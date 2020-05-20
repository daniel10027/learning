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
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect


class TutorSignUpView(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'TUTEUR'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        type =  'Tuteur'
        current_site = get_current_site(self.request)
        mail_subject = 'Activation Compte '+ type + ' EduvRoom.'
        message = render_to_string("msg.html"
        , {
            'user':user,
            'domain': current_site.domain,
            'type': type
                        
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                                mail_subject, message, to=[to_email]
                    )
        email.send()
        messages.success(self.request, f'Le compte Tuteur  a été crée avec succes!')
        return HttpResponseRedirect(self.request.path_info)



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