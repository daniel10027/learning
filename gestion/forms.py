from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from recrutement.models import Resultat
from .models import Student, Enseignant, Tuteur, User,Domaine
from django.forms.widgets import CheckboxSelectMultiple

################STUDENT REGISTER FORM#################
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
######################################################




#################ENSEIGNANT REGISTER FORM#############
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

class TeacherUpdateForm(forms.ModelForm):
      class Meta:
        model  = Enseignant
        fields = ["matricule","structure","localite","contact","grade","domaine","photo","piece_indentite"]
      def __init__(self, *args, **kwargs):
          super( TeacherUpdateForm, self).__init__(*args, **kwargs)
          self.fields["domaine"].widget = CheckboxSelectMultiple()
          self.fields["domaine"].queryset = Domaine.objects.all()
class TeacherUserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
######################################################


################# TUTEUR REGISTER FORM################
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

######################################################
class  ResultatForm(forms.ModelForm):
    class Meta:
        model = Resultat
        fields = ['critere1','critere2','critere3','critere4','critere5',]