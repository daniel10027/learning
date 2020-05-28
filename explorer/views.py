import re
import six
from collections import Counter

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

import django
from django.db import DatabaseError
from django.db.models import Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, render
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME

if django.VERSION >= (1, 11):
    from django.contrib.auth.views import LoginView

from explorer import app_settings
from explorer.connections import connections
from explorer.exporters import get_exporter_class
from explorer.forms import QueryForm
from explorer.models import Query, QueryLog, MSG_FAILED_BLACKLIST
from explorer.tasks import execute_query
from explorer.utils import (
    url_get_rows,
    url_get_query_id,
    url_get_log_id,
    url_get_params,
    safe_login_prompt,
    fmt_sql,
    allowed_query_pks,
    url_get_show,
    url_get_fullscreen
)

from explorer.schema import schema_info
from explorer import permissions


class ExplorerContextMixin(object):

    def gen_ctx(self):
        return {'can_view': app_settings.EXPLORER_PERMISSION_VIEW(self.request.user),
                'can_change': app_settings.EXPLORER_PERMISSION_CHANGE(self.request.user)}

    def get_context_data(self, **kwargs):
        ctx = super(ExplorerContextMixin, self).get_context_data(**kwargs)
        ctx.update(self.gen_ctx())
        return ctx

    def render_template(self, template, ctx):
        ctx.update(self.gen_ctx())
        return render(self.request, template, ctx)


class PermissionRequiredMixin(object):

    permission_required = None

    def get_permission_required(self):
        if self.permission_required is None:
            raise ImproperlyConfigured(
                '{0} is missing the permission_required attribute. Define {0}.permission_required, or override '
                '{0}.get_permission_required().'.format(self.__class__.__name__)
            )
        return self.permission_required

    def has_permission(self, request, *args, **kwargs):
        perms = self.get_permission_required()
        handler = getattr(permissions, perms)  # TODO: fix the case when the perms is
                                               # not defined in permissions module.
        return handler(request, *args, **kwargs)

    def handle_no_permission(self, request):
        if django.VERSION >= (1, 11):
            return SafeLoginView.as_view(
                extra_context={'title': 'Log in', REDIRECT_FIELD_NAME: request.get_full_path()})(request)
        return safe_login_prompt(request)

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission(request, *args, **kwargs):
            return self.handle_no_permission(request)
        return super(PermissionRequiredMixin, self).dispatch(request, *args, **kwargs)


if django.VERSION > (1, 11):
    class SafeLoginView(LoginView):
        template_name = 'admin/login.html'


def _export(request, query, download=True):
    format = request.GET.get('format', 'csv')
    exporter_class = get_exporter_class(format)
    query.params = url_get_params(request)
    delim = request.GET.get('delim')
    exporter = exporter_class(query)
    try:
        output = exporter.get_output(delim=delim)
    except DatabaseError as e:
        msg = "Error executing query %s: %s" % (query.title, e)
        return HttpResponse(msg, status=500)
    response = HttpResponse(output, content_type=exporter.content_type)
    if download:
        response['Content-Disposition'] = 'attachment; filename="%s"' % (
            exporter.get_filename()
        )
    return response


class DownloadQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query)


class DownloadFromSqlView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, *args, **kwargs):
        sql = request.POST.get('sql')
        connection = request.POST.get('connection')
        query = Query(sql=sql, connection=connection, title='')
        ql = query.log(request.user)
        query.title = 'Playground - %s' % ql.id
        return _export(request, query)


class StreamQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id, *args, **kwargs):
        query = get_object_or_404(Query, pk=query_id)
        return _export(request, query, download=False)


class EmailCsvQueryView(PermissionRequiredMixin, View):

    permission_required = 'view_permission'

    def post(self, request, query_id, *args, **kwargs):
        if request.is_ajax():
            email = request.POST.get('email', None)
            if email:
                execute_query.delay(query_id, email)
                return JsonResponse({'message': 'message was sent successfully'})
        return JsonResponse({}, status=403)


class SchemaView(PermissionRequiredMixin, View):
    permission_required = 'change_permission'

    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, *args, **kwargs):
        return super(SchemaView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        connection = kwargs.get('connection')
        if connection not in connections:
            raise Http404
        schema = schema_info(connection)
        if schema:
            return render('explorer/schema.html',
                                      {'schema': schema_info(connection)})
        else:
            return render('explorer/schema_building.html')


@require_POST
def format_sql(request):
    sql = request.POST.get('sql', '')
    formatted = fmt_sql(sql)
    return JsonResponse({"formatted": formatted})


class ListQueryView(PermissionRequiredMixin, ExplorerContextMixin, ListView):

    permission_required = 'view_permission_list'

    def recently_viewed(self):
        qll = QueryLog.objects.filter(run_by_user=self.request.user, query_id__isnull=False).order_by(
            '-run_at').select_related('query')
        ret = []
        tracker = []
        for ql in qll:
            if len(ret) == app_settings.EXPLORER_RECENT_QUERY_COUNT:
                break

            if ql.query_id not in tracker:
                ret.append(ql)
                tracker.append(ql.query_id)
        return ret

    def get_context_data(self, **kwargs):
        context = super(ListQueryView, self).get_context_data(**kwargs)
        context['object_list'] = self._build_queries_and_headers()
        context['recent_queries'] = self.recently_viewed()
        context['tasks_enabled'] = app_settings.ENABLE_TASKS
        return context

    def get_queryset(self):
        if app_settings.EXPLORER_PERMISSION_VIEW(self.request.user):
            qs = Query.objects.prefetch_related('created_by_user').all()
        else:
            qs = Query.objects.prefetch_related('created_by_user').filter(pk__in=allowed_query_pks(self.request.user.id))
        return qs.annotate(run_count=Count('querylog'))

    def _build_queries_and_headers(self):
        """
        Build a list of query information and headers (pseudo-folders) for consumption by the template.

        Strategy: Look for queries with titles of the form "something - else" (eg. with a ' - ' in the middle)
                  and split on the ' - ', treating the left side as a "header" (or folder). Interleave the
                  headers into the ListView's object_list as appropriate. Ignore headers that only have one
                  child. The front end uses bootstrap's JS Collapse plugin, which necessitates generating CSS
                  classes to map the header onto the child rows, hence the collapse_target variable.

                  To make the return object homogeneous, convert the object_list models into dictionaries for
                  interleaving with the header "objects". This necessitates special handling of 'created_at'
                  and 'created_by_user' because model_to_dict doesn't include non-editable fields (created_at)
                  and will give the int representation of the user instead of the string representation.

        :return: A list of model dictionaries representing all the query objects, interleaved with header dictionaries.
        """

        dict_list = []
        rendered_headers = []
        pattern = re.compile('[\W_]+')

        headers = Counter([q.title.split(' - ')[0] for q in self.object_list])

        for q in self.object_list:
            model_dict = model_to_dict(q)
            header = q.title.split(' - ')[0]
            collapse_target = pattern.sub('', header)

            if headers[header] > 1 and header not in rendered_headers:
                dict_list.append({'title': header,
                                  'is_header': True,
                                  'is_in_category': False,
                                  'collapse_target': collapse_target,
                                  'count': headers[header]})
                rendered_headers.append(header)

            model_dict.update({'is_in_category': headers[header] > 1,
                               'collapse_target': collapse_target,
                               'created_at': q.created_at,
                               'is_header': False,
                               'run_count': q.run_count,
                               'created_by_user': six.text_type(q.created_by_user) if q.created_by_user else None})
            dict_list.append(model_dict)
        return dict_list

    model = Query


class ListQueryLogView(PermissionRequiredMixin, ExplorerContextMixin, ListView):

    permission_required = 'view_permission'

    def get_queryset(self):
        kwargs = {'sql__isnull': False}
        if url_get_query_id(self.request):
            kwargs['query_id'] = url_get_query_id(self.request)
        return QueryLog.objects.filter(**kwargs).all()

    context_object_name = "recent_logs"
    model = QueryLog
    paginate_by = 20


class CreateQueryView(PermissionRequiredMixin, ExplorerContextMixin, CreateView):

    permission_required = 'change_permission'

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user
        return super(CreateQueryView, self).form_valid(form)

    form_class = QueryForm
    template_name = 'explorer/query.html'


class DeleteQueryView(PermissionRequiredMixin, ExplorerContextMixin, DeleteView):

    permission_required = 'change_permission'
    model = Query
    success_url = reverse_lazy("explorer_index")


class PlayQueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'change_permission'

    def get(self, request):
        if url_get_query_id(request):
            query = get_object_or_404(Query, pk=url_get_query_id(request))
            return self.render_with_sql(request, query, run_query=False)

        if url_get_log_id(request):
            log = get_object_or_404(QueryLog, pk=url_get_log_id(request))
            query = Query(sql=log.sql, title="Playground", connection=log.connection)
            return self.render_with_sql(request, query)

        return self.render()

    def post(self, request):
        sql = request.POST.get('sql')
        show = url_get_show(request)
        query = Query(sql=sql, title="Playground", connection=request.POST.get('connection'))
        passes_blacklist, failing_words = query.passes_blacklist()
        error = MSG_FAILED_BLACKLIST % ', '.join(failing_words) if not passes_blacklist else None
        run_query = not bool(error) if show else False
        return self.render_with_sql(request, query, run_query=run_query, error=error)

    def render(self):
        return self.render_template('explorer/play.html', {'title': 'Playground', 'form': QueryForm()})

    def render_with_sql(self, request, query, run_query=True, error=None):
        rows = url_get_rows(request)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'play'
        form = QueryForm(request.POST if len(request.POST) else None, instance=query)
        return self.render_template('explorer/%s.html' % template, query_viewmodel(request.user,
                                                                                   query,
                                                                                   title="Playground",
                                                                                   run_query=run_query,
                                                                                   error=error,
                                                                                   rows=rows,
                                                                                   form=form))


class QueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'view_permission'

    def get(self, request, query_id):
        query, form = QueryView.get_instance_and_form(request, query_id)
        query.save()  # updates the modified date
        show = url_get_show(request)
        rows = url_get_rows(request)
        vm = query_viewmodel(request.user, query, form=form, run_query=show, rows=rows)
        fullscreen = url_get_fullscreen(request)
        template = 'fullscreen' if fullscreen else 'query'
        return self.render_template('explorer/%s.html' % template, vm)

    def post(self, request, query_id):
        if not app_settings.EXPLORER_PERMISSION_CHANGE(request.user):
            return HttpResponseRedirect(
                reverse_lazy('query_detail', kwargs={'query_id': query_id})
            )
        show = url_get_show(request)
        query, form = QueryView.get_instance_and_form(request, query_id)
        success = form.is_valid() and form.save()
        vm = query_viewmodel(request.user,
                             query,
                             form=form,
                             run_query=show,
                             rows=url_get_rows(request),
                             message="Query saved." if success else None)
        return self.render_template('explorer/query.html', vm)

    @staticmethod
    def get_instance_and_form(request, query_id):
        query = get_object_or_404(Query, pk=query_id)
        query.params = url_get_params(request)
        form = QueryForm(request.POST if len(request.POST) else None, instance=query)
        return query, form


def query_viewmodel(user, query, title=None, form=None, message=None, run_query=True, error=None, rows=app_settings.EXPLORER_DEFAULT_ROWS):
    res = None
    ql = None
    if run_query:
        try:
            res, ql = query.execute_with_logging(user)
        except DatabaseError as e:
            error = str(e)
    has_valid_results = not error and res and run_query
    ret = {
        'tasks_enabled': app_settings.ENABLE_TASKS,
        'params': query.available_params(),
        'title': title,
        'shared': query.shared,
        'query': query,
        'form': form,
        'message': message,
        'error': error,
        'rows': rows,
        'data': res.data[:rows] if has_valid_results else None,
        'headers': res.headers if has_valid_results else None,
        'total_rows': len(res.data) if has_valid_results else None,
        'duration': res.duration if has_valid_results else None,
        'has_stats': len([h for h in res.headers if h.summary]) if has_valid_results else False,
        'snapshots': query.snapshots if query.snapshot else [],
        'ql_id': ql.id if ql else None,
        'unsafe_rendering': app_settings.UNSAFE_RENDERING,
    }
    return ret
