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
        if request.user.is_teacher:
            return redirect('teachers:quiz_change_list')
        elif request.user.is_student:
            return render(request, 'enseignement/index.html', context)
        else:
            pass
    return render(request, 'enseignement/index.html', context)

def contact(request):
    return render(request, 'enseignement/contact.html')