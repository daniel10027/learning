import functools
import re

from django.contrib.auth.forms import AuthenticationForm

try:
    from django.contrib.auth.views import login
except ImportError:
    pass

from django.contrib.auth import REDIRECT_FIELD_NAME
from six import text_type
import sqlparse

from explorer import app_settings

EXPLORER_PARAM_TOKEN = "$$"


def passes_blacklist(sql):
    clean = functools.reduce(lambda sql, term: sql.upper().replace(term, ""), [t.upper() for t in app_settings.EXPLORER_SQL_WHITELIST], sql)
    fails = [bl_word for bl_word in app_settings.EXPLORER_SQL_BLACKLIST if bl_word in clean.upper()]
    return not any(fails), fails


def _format_field(field):
    return field.get_attname_column()[1], field.get_internal_type()


def param(name):
    return "%s%s%s" % (EXPLORER_PARAM_TOKEN, name, EXPLORER_PARAM_TOKEN)


def swap_params(sql, params):
    p = params.items() if params else {}
    for k, v in p:
        regex = re.compile("\$\$%s(?:\:([^\$]+))?\$\$" % str(k).lower(), re.I)
        sql = regex.sub(text_type(v), sql)
    return sql


def extract_params(text):
    regex = re.compile("\$\$([a-z0-9_]+)(?:\:([^\$]+))?\$\$")
    params = re.findall(regex, text.lower())
    return {p[0]: p[1] if len(p) > 1 else '' for p in params}


def safe_login_prompt(request):
    defaults = {
        'template_name': 'admin/login.html',
        'authentication_form': AuthenticationForm,
        'extra_context': {
            'title': 'Log in',
            'app_path': request.get_full_path(),
            REDIRECT_FIELD_NAME: request.get_full_path(),
        },
    }
    return login(request, **defaults)


def shared_dict_update(target, source):
    for k_d1 in target:
        if k_d1 in source:
            target[k_d1] = source[k_d1]
    return target


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except ValueError:
        return default


def get_int_from_request(request, name, default):
    val = request.GET.get(name, default)
    return safe_cast(val, int, default) if val else None


def get_params_from_request(request):
    val = request.GET.get('params', None)
    try:
        d = {}
        tuples = val.split('|')
        for t in tuples:
            res = t.split(':')
            d[res[0]] = res[1]
        return d
    except Exception:
        return None


def get_params_for_url(query):
    if query.params:
        return '|'.join(['%s:%s' % (p, v) for p, v in query.params.items()])


def url_get_rows(request):
    return get_int_from_request(request, 'rows', app_settings.EXPLORER_DEFAULT_ROWS)


def url_get_query_id(request):
    return get_int_from_request(request, 'query_id', None)


def url_get_log_id(request):
    return get_int_from_request(request, 'querylog_id', None)


def url_get_show(request):
    return bool(get_int_from_request(request, 'show', 1))


def url_get_fullscreen(request):
    return bool(get_int_from_request(request, 'fullscreen', 0))


def url_get_params(request):
    return get_params_from_request(request)


def allowed_query_pks(user_id):
    return app_settings.EXPLORER_GET_USER_QUERY_VIEWS().get(user_id, [])


def user_can_see_query(request, **kwargs):
    # In Django<1.10, is_anonymous was a method.
    try:
        is_anonymous = request.user.is_anonymous()
    except TypeError:
        is_anonymous = request.user.is_anonymous
    if not is_anonymous and 'query_id' in kwargs:
        return int(kwargs['query_id']) in allowed_query_pks(request.user.id)
    return False


def fmt_sql(sql):
    return sqlparse.format(sql, reindent=True, keyword_case='upper')


def noop_decorator(f):
    return f


class InvalidExplorerConnectionException(Exception):
    pass


def get_valid_connection(alias=None):
    from explorer.connections import connections

    if not alias:
        return connections[app_settings.EXPLORER_DEFAULT_CONNECTION]

    if alias not in connections:
        raise InvalidExplorerConnectionException(
            'Attempted to access connection %s, but that is not a registered Explorer connection.' % alias
        )
    return connections[alias]


def get_s3_bucket():
    from boto.s3.connection import S3Connection

    conn = S3Connection(app_settings.S3_ACCESS_KEY,
                        app_settings.S3_SECRET_KEY)
    return conn.get_bucket(app_settings.S3_BUCKET)


def s3_upload(key, data):
    from boto.s3.key import Key
    bucket = get_s3_bucket()
    k = Key(bucket)
    k.key = key
    k.set_contents_from_file(data, rewind=True)
    k.set_acl('public-read')
    k.set_metadata('Content-Type', 'text/csv')
    return k.generate_url(expires_in=0, query_auth=False)

