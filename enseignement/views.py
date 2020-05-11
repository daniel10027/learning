from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from recrutement.models import Recrutement

# Create your views here.
def home(request): # pour afficher les produits a vendre sur l_index
    context = {
         'recrutements': Recrutement.objects.all()
         }
    if request.user.is_authenticated:
        if request.user.is_teacher or request.user.is_staff :
            return redirect('teachers:accueil-teacher')
        elif request.user.is_student:
            return render(request, 'enseignement/index.html', context)
        elif request.user.is_tutor:
            return redirect('tutors:accueil-tutor')
    return render(request, 'enseignement/index.html', context)

def contact(request):
    return render(request, 'enseignement/contact.html')