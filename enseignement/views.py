from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def home(request): # pour afficher les produits a vendre sur l_index
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        elif request.user.is_student:
            return redirect('students:accueil-student')
        else:
            pass
    return render(request, 'enseignement/index.html')