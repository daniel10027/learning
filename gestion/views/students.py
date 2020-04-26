from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView

from ..decorators import student_required
from ..forms import StudentSignUpForm
from ..models import Student, User
from enseignement.models import Cours, UniteEnseignement, Ecue, RessourcePdf, RessourceVideo


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ETUDIANT'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        return redirect('login-student')


@method_decorator([login_required, student_required], name='dispatch')
class StudentsEcuesView(ListView):
    model = Ecue
    template_name = 'enseignement/course.html'
    context_object_name = 'ecues'
    ordering = ['-created']
    paginate_by = 4


@method_decorator([login_required, student_required], name='dispatch')
class StudentsCoursListView(ListView):
    model = Cours
    template_name = 'enseignement/course_list.html'
    context_object_name = 'cours'
    ordering = ['-created']
    paginate_by = 4

    def get_queryset(self):
        ecues = get_object_or_404(Ecue, pk=self.kwargs.get('pk'))
        return Cours.objects.filter(ecue=ecues).order_by('-created')

@method_decorator([login_required, student_required], name='dispatch')
class StudentsCoursDetailView(DetailView):
    model = Cours
    template_name = 'enseignement/course_detail.html'
    def get_context_data(self, **kwargs):
        context = super(StudentsCoursDetailView, self).get_context_data(**kwargs)
        context['pdfs'] = RessourcePdf.objects.all()
        context['videos'] = RessourceVideo.objects.all()
        return context

