from django import forms
from django.forms.models import BaseInlineFormSet
from django.forms import ModelForm
from .models import DossierRecrutement, Diplome,Certificat
from django.forms.models import inlineformset_factory
from django.forms.widgets import CheckboxSelectMultiple



class DossierRecrutementForm(ModelForm):
       class Meta:
        model = DossierRecrutement
        fields = ["nom","prenom","date_de_naissance","sexe","localite","email","grade","domaine","contact","photo","piece_indentite"]
       def __init__(self, *args, **kwargs):
        
            super(DossierRecrutementForm, self).__init__(*args, **kwargs)
            self.fields["domaine"].widget = CheckboxSelectMultiple()
            self.fields["domaine"].queryset = Domaine.objects.all()

class DiplomeForm(ModelForm):

    class Meta:
        model = Diplome
        exclude = ("status","created","fichier")
    

class CertificatForm(ModelForm):

    class Meta:
        model = Certificat
        exclude = ("status","created","documents")

DiplomeFormSet = inlineformset_factory(DossierRecrutement, Diplome,form=DiplomeForm,extra=1)
CertificatFormSet = inlineformset_factory(DossierRecrutement, Certificat,form=CertificatForm,extra=1)


