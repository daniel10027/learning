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


#################################################################################
#################################################################################
class RecrutementListView(ListView):
    model = Recrutement
    context_object_name = 'recrutements'
    template_name = 'recrutement/index.html'
    ordering = ['-created']
    paginate_by = 4
   
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
    fields = ["nom","prenom", "date_de_naissance",
                "sexe","localite","email","grade",
                "domaine","contact","photo","piece_indentite","lettre_motivation"]
    #template_name = 'recrutement/dossierrecrutement_form.html'
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
        messages.success(self.request, f'Votre Dossier a été enrégistré avec succes  .')
        return super(DossierRecrutementCreateView, self).form_valid(form)
#####################################################################################
#####################################################################################

class DossierRecrutementCreateViews(CreateView):
    model = DossierRecrutement
    template_name = 'recrutement/dossierrecrutement_form.html'
    form_class = DossierRecrutementForm
    success_url = reverse_lazy('recrutement-home')
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        diplomes = DiplomeFormSet()
        certificats = CertificatFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  diplomes=diplomes,
                                  certificats=certificats))
    
    def post(self, request, *args, **kwargs):
        
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        diplomes = DiplomeFormSet(self.request.POST, prefix="diplomes")
        certificats = CertificatFormSet(self.request.POST, prefix="certificats")
        if (form.is_valid() and diplomes.is_valid() and  certificats.is_valid()):
            return self.form_valid(form, diplomes, certificats)
        else:
            return self.form_invalid(form, diplomes, certificats)
    

    def form_valid(self, form, diplomes, certificats, **kwargs):
  
        with transaction.atomic():
            form.instance.recrutement_id = self.kwargs['pk']
            self.object = form.save()
            diplomes.instance = self.object
            diplomes.save()
            certificats.instance = self.object
            certificats.save()
        return super(DossierRecrutementCreateViews, self).form_valid(form)

    def form_invalid(self, form, diplomes, certificats):
       
        return self.render_to_response(
            self.get_context_data(form=form,
                                  diplomes=diplomes,
                                  certificats=certificats))
#####################################################################################
#####################################################################################


