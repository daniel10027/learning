from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import student_required
from ..forms import StudentSignUpForm
from ..models import Student, User
from enseignement.models import Cours, UniteEnseignement, Ecue


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
        username = form.cleaned_data.get('username')
        messages.success(request, f'Félicitation  {username} , vous pouvez vous Connecter.')
        return redirect('login-student')


@method_decorator([login_required, student_required], name='dispatch')
class StudentsEcuesView(ListView):
    model = Ecue
    template_name = 'enseignement/course.html'
    context_object_name = 'ecues'
    ordering = ['-created']
    paginate_by = 4

