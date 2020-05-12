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
from ..forms import TutorSignUpForm, TutorProfile, TutorUser
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
def home(request): 
    return render(request, 'gestion/index.html')

#######################################################################################################################################
@login_required
@tutor_required
def TutorProfilet(request):
     if request.method == 'POST':
        user_form = TutorUser(request.POST, instance=request.user)
        profile_form = TutorProfile(request.POST, 
                                   request.FILES, 
                                   instance=request.user.tuteur)
        if  user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Votre Profile a été mis à jour avec succes !')
            return redirect('tutors:tutor-profile')
        else:
            messages.error(request, f'Une erreur est survenue au cours de la mise a jour!')
     else:
        user_form = TutorUser(instance=request.user)
        profile_form = TutorProfile(instance=request.user.tuteur)
       
       
     context = {
        'user_form': user_form,
        'profile_form' : profile_form
     }
    
     return render(request, 'gestion/profilet.html', context)   

                                                



#######################################################################################################################