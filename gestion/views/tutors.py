from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import tutor_required
from ..forms import TutorSignUpForm
from ..models import Tuteur, User


class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'TUTEUR'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')



@login_required
@tutor_required
def home(request): # pour afficher les produits a vendre sur l_index
    return render(request, 'gestion/index.html')