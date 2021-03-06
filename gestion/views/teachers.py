from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from ..decorators import teacher_required
from ..forms import TeacherSignUpForm, ResultatForm, TeacherUpdateForm, TeacherUserUpdate
from ..models import Enseignant, User
from recrutement.models import DossierRecrutement, Resultat, Jury, Diplome, Certificat, Recrutement, Critere
from django.db.models import Avg, query
from django.db import connection
import itertools
from configuration.models import Message

from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect


###############################################################
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'ENSEIGNANT'
        return super().get_context_data(**kwargs)
        

    def form_valid(self, form):
        
        user = form.save()
        type =  'Enseignant'
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
       
        messages.success(self.request, f'Le compte Enseignant a été crée avec succes!')
        return HttpResponseRedirect(self.request.path_info)

   
################################################################

@login_required
@teacher_required
def home(request): # pour afficher les produits a vendre sur l_index
    context = {
          'jurys': Jury.objects.all(),
           'msg': Message.objects.all()
    }
    return render(request, 'gestion/index.html', context)

###############################################################
@method_decorator([login_required, teacher_required ], name='dispatch')
class JuryListView(ListView):
    model = Jury
    ordering = ('-created', )
    context_object_name = 'jurys'
    template_name = 'gestion/index.html'
    def get_context_data(self, **kwargs):
        context = super(JuryListView, self).get_context_data(**kwargs)
        context['dossier']    = DossierRecrutement.objects.all()
        context['recru']    = Recrutement.objects.all()
        context['msg']    = Message.objects.all()
        return context
    

################################################################
@method_decorator([login_required, teacher_required ], name='dispatch')
class DossierListView(ListView):
    model = DossierRecrutement
    ordering = ('-created', )
    context_object_name = 'dossiers'
    template_name = 'gestion/dossier_list.html'
    def get_context_data(self, **kwargs):
        context = super(DossierListView, self).get_context_data(**kwargs)
        context['jurys']    = Jury.objects.all()
        
        return context
    def get_queryset(self):
        recru = get_object_or_404(Recrutement, pk=self.kwargs.get('pk'))
        res=  DossierRecrutement.objects.filter(recrutement=recru)
        return res
################################################################

class DossierDetailView(DetailView):
    model = DossierRecrutement
    template_name = "gestion/dossier_detail.html"
    def get_context_data(self, **kwargs):
        context = super(DossierDetailView, self).get_context_data(**kwargs)
        context['diplomes']    = Diplome.objects.all()
        context['certificats'] = Certificat.objects.all()
        context['forms'] = ResultatForm()
        context['criteres'] = Critere.objects.all()
        return context
    
####################################################################
class ResulatCreateView(CreateView):
    model = Resultat
    form_class = ResultatForm
    success_url = reverse_lazy('teachers:accueil-teacher')
    def get_context_data(self, **kwargs):
        data = super(ResulatCreateView, self).get_context_data(**kwargs)
    def form_valid(self, form, *args, **kwargs):
        context = self.get_context_data()
        with transaction.atomic():
            form.instance.dossier_id = self.kwargs['pk']
            form.instance.juge_id = self.request.user.enseignant.id
            self.object = form.save()
            print(self.request.user.id)
        
        messages.success(self.request, f'Les résultat ont été tramis avec succes .')
          
        return super(ResulatCreateView, self).form_valid(form)
################################################################################
################################################################################

###################################################################################
###################################################################################
class RecrutementListView(ListView):
    model = Recrutement
    context_object_name = 'recrutements'
    template_name = 'gestion/recrutement_list.html'
    ordering = ['-created']
    paginate_by = 2
   
#########################################PROFILE##############################
@login_required
@teacher_required
def profile(request): # pour afficher les produits a vendre sur l_index
     if request.method == 'POST':
        u_form = TeacherUserUpdate(request.POST, instance=request.user)
        p_form = TeacherUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.enseignant)
        if  u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre Profile a été mis à jour avec succes !')
            return redirect('teachers:teacher-profile')
        else:
            messages.error(request, f'Une erreur est survenue au cours de la mise a jour!')
     else:
        u_form = TeacherUserUpdate(instance=request.user)
        p_form = TeacherUpdateForm(instance=request.user.enseignant)
       
       
     context = {
        'u_form': u_form,
        'p_form' : p_form
     }
    
     return render(request, 'gestion/profile.html', context)
###################################################################################

@method_decorator([login_required, teacher_required ], name='dispatch')
class ResultatFinal(ListView):
    model = Resultat
    ordering = ('-Moyenne', )
    context_object_name = 'resultat'
    template_name = 'gestion/resultat.html'
    def get_queryset(self):
        recru = get_object_or_404(Recrutement, pk=self.kwargs.get('pk'))
        res=  sorted(Resultat.objects.filter(dossier__recrutement=recru).distinct("dossier"), key=lambda t: t.All)
        return res
        
#######################################STATISTIQUESS#######################################
@method_decorator([login_required, teacher_required ], name='dispatch')

class Reclist(ListView):
    model = Recrutement
    context_object_name = 'recrutements'
    template_name = 'gestion/stat_list.html'
    ordering = ['-created']
    paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super(Reclist, self).get_context_data(**kwargs)
        context['dossier']    = DossierRecrutement.objects.all()
        return context

#################################################################################
#################################################################################
@method_decorator([login_required, teacher_required ], name='dispatch')
class DossierListViewA(ListView):
    model = DossierRecrutement
    ordering = ('-created', )
    context_object_name = 'dossiers'
    template_name = 'gestion/rec_dossier_list.html'
    def get_queryset(self):
        recru = get_object_or_404(Recrutement, pk=self.kwargs.get('pk'))
        res=  DossierRecrutement.objects.filter(recrutement=recru)
        return res