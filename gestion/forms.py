from django import forms
import os
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from recrutement.models import Resultat
from .models import Student, Enseignant, Tuteur, User,Domaine
from django.forms.widgets import CheckboxSelectMultiple
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
################STUDENT REGISTER FORM###############################################################################
class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',"last_name","first_name","email"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user

################# ENSEIGNANT REGISTER FORM #########################################################################
class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',"last_name","first_name","email"]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        enseignant = Enseignant.objects.create(user=user)
        return user
####################################################################################################################
################# TUTEUR REGISTER FORM############################################################################
class TutorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username',"last_name","first_name","email"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        user.save()
        tuteur = Tuteur.objects.create(user=user)
        return user



################# ENSEIGNANT PROFILE UPDATE ########################################################################
class TeacherUpdateForm(forms.ModelForm):
      class Meta:
        model  = Enseignant
        fields = ["matricule","sexe","structure","localite","contact","date_de_naissance","grade","domaine","photo","piece_indentite"]
      def __init__(self, *args, **kwargs):
          super( TeacherUpdateForm, self).__init__(*args, **kwargs)
          self.fields["domaine"].widget = CheckboxSelectMultiple()
          self.fields["domaine"].queryset = Domaine.objects.all()
     
            
          
################# ENSEIGNANT USER UPDATE ############# ############################################################        
class TeacherUserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

##################RESULATAT FORM FOR EACH TEACHER ###############################################################
class  ResultatForm(forms.ModelForm):
    class Meta:
        model = Resultat
        fields = ['critere1','critere2','critere3','critere4','critere5',]
    
###################################################################
################# TUTEUR PROFILE UPDATE ########################################################################
class TutorProfile(forms.ModelForm):
      class Meta:
        model  = Tuteur
        fields = ["date_de_naissance","sexe","structure","localite","contact","domaine","photo","piece_indentite"]
      def __init__(self, *args, **kwargs):
          super( TutorProfile, self).__init__(*args, **kwargs)
          self.fields["domaine"].widget = CheckboxSelectMultiple()
          self.fields["domaine"].queryset = Domaine.objects.all()
     
            
          
################# TUTEUR USER UPDATE ############# ############################################################        
class TutorUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
################# Student PROFILE UPDATE ########################################################################
class StudentUpdateForm(forms.ModelForm):
      class Meta:
        model  = Student
        fields = ["date_de_naissance","sexe","localite","contact","photo","piece_indentite"]
     
     
            
          
################# student USER UPDATE ############# ############################################################        
class StudentUserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']