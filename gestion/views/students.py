from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string

from ..decorators import student_required
from ..forms import StudentSignUpForm,StudentUpdateForm, StudentUserUpdate
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
        type =  'Etudiant'
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
        login(self.request, user)
        
        return redirect('login')


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



@login_required
@student_required
def profile(request): # pour afficher les produits a vendre sur l_index
     if request.method == 'POST':
        u_form = StudentUserUpdate(request.POST, instance=request.user)
        p_form = StudentUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.student)
        if  u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre Profile a été mis à jour avec succes !')
            return redirect('students:student-profile')
        else:
            messages.error(request, f'Une erreur est survenue au cours de la mise a jour!')
     else:
        u_form = StudentUserUpdate(instance=request.user)
        p_form = StudentUpdateForm(instance=request.user.student)
       
       
     context = {
        'u_form': u_form,
        'p_form' : p_form
     }
    
     return render(request, 'enseignement/profile.html', context)