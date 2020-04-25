from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import Student, Enseignant, Tuteur, User

################STUDENT REGISTER FORM#################
class StudentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        enseignant = Enseignant.objects.create(user=user)
        return user
        
######################################################
################# TUTEUR REGISTER FORM################
class TutorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_tutor = True
        user.save()
        tuteur = Tuteur.objects.create(user=user)
        return user

######################################################
        