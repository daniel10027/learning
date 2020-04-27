from django import forms
from django.forms.models import BaseInlineFormSet
from django.forms import ModelForm
from .models import DossierRecrutement, Diplome,Certificat
from django.forms.models import inlineformset_factory

class DiplomeForm(ModelForm):

    class Meta:
        model = Diplome
        exclude = ["status"]
    
DiplomeFormSet = inlineformset_factory(
    DossierRecrutement, Diplome,
    form=DiplomeForm,
    extra=1  
)

class CertificatForm(ModelForm):

    class Meta:
        model = Certificat
        exclude = ["status"]
    
CertificatFormSet = inlineformset_factory(
    DossierRecrutement, Certificat,
    form=CertificatForm,
    extra=1   
)