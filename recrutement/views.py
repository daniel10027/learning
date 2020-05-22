from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView
# Create your views here.
from .models import Recrutement, DossierRecrutement, Diplome, Certificat, Resultat, Jury
from .forms import DiplomeFormSet, CertificatFormSet, DossierRecrutementForm
from datetime import datetime
from django.views.generic.edit import FormMixin

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site

#################################################################################
#################################################################################
class RecrutementListView(ListView):
    model = Recrutement
    context_object_name = 'recrutements'
    template_name = 'recrutement/index.html'
    ordering = ['-created']
    paginate_by = 2
   
#################################################################################
#################################################################################
class RecrutementDetailView(DetailView):
    model = Recrutement 
    context_object_name = 'recrutements'
    template_name = 'recrutement/recrutement_detail.html'
    def get_context_data(self, **kwargs):
        context = super(RecrutementDetailView, self).get_context_data(**kwargs)
        return context

    
    
################################################################################
class DossierRecrutementCreate(CreateView):
    model = DossierRecrutement
    fields = ["nom","prenom", "date_de_naissance",
                "sexe","localite","email","grade",
                "domaine","contact","photo"," piece_indentite","lettre_motivation"]
################################################################################

class DossierRecrutementCreateView(CreateView):
    model = DossierRecrutement
    fields = ["nom","prenom", "date_de_naissance","sexe","localite","email","grade","domaine","contact","photo","piece_indentite","lettre_motivation"]
    
    success_url = reverse_lazy('recrutement-home')
    def get_context_data(self, **kwargs):
        data = super(DossierRecrutementCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            data['diplomes']    = DiplomeFormSet(self.request.POST, self.request.FILES, prefix="diplome_set")
            data['certificats'] = CertificatFormSet(self.request.POST, self.request.FILES, prefix="certificat_set")
        else:
            data['diplomes']    = DiplomeFormSet(prefix="diplome_set")
            data['certificats'] = CertificatFormSet(prefix="certificat_set")
        return data

    def form_valid(self, form, *args, **kwargs):
        context = self.get_context_data()
        diplomes = context['diplomes']
        certificats = context['certificats'] 
        with transaction.atomic():
            form.instance.recrutement_id = self.kwargs['pk']
            self.object = form.save()

        if diplomes.is_valid()  :
                diplomes.instance = self.object
                diplomes.save()
        if certificats.is_valid():
                certificats.instance = self.object
                certificats.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Inscription au recrutement EduvRoom.'
        nom = form.cleaned_data.get('nom')
        prenom = form.cleaned_data.get('prenom')
        to_email = form.cleaned_data.get('email')
        message = render_to_string("recru.html"
        , {
            'nom':nom,
            'prenom':prenom,
            'email':to_email
            
                        
        })
        
        email = EmailMessage(
                                mail_subject, message, to=[to_email]
                    )
        email.send()
        messages.success(self.request, f'Votre Dossier a été enrégistré avec succes , un message de confirmation vous a été envoyé par Email .')
        return super(DossierRecrutementCreateView, self).form_valid(form)
#####################################################################################
#####################################################################################
