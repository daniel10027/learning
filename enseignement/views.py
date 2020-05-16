from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMessage
from recrutement.models import Recrutement
from configuration.models import Partenaire, CopyRight, ContactInfo, Message
from .forms import Contact_Form
# Create your views here.
def home(request): # pour afficher les produits a vendre sur l_index
    context = {
         'recrutements': Recrutement.objects.all(),
         'partenaires': Partenaire.objects.all(),
         'copy': CopyRight.objects.all(),
         'msg': Message.objects.all()

         }
    if request.user.is_authenticated:
        if request.user.is_teacher or request.user.is_staff :
            return redirect('teachers:accueil-teacher')
        elif request.user.is_student:
            return redirect('students:accueil-student')
        elif request.user.is_tutor:
            return redirect('tutors:accueil-tutor')
    return render(request, 'enseignement/index.html', context)

def contact(request):
    
    context = {
         
         'contact': ContactInfo.objects.all(),
         'form': Contact_Form,

         }
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            nom = request.POST.get('nom')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            template = get_template('enseignement/contact_form.txt')
            context = {
                'nom' : nom,
                'email' : email,
               
                'message' : message,
            }
            content = template.render(context)

            email = EmailMessage(
                "Nouveau Message depuis EduvRoom",
                content,
                "EduvRoom" + '', 
                ['Danielguedegbe10027@gmail.com'],
                headers = { 'Reply To': email }
            )

            email.send()
            messages.success(request, f'Votre Message a bien été envoyé, Nous vous contacterons dans un bref delai .Merci ')
            return render(request, 'enseignement/msg.html')
    return render(request, 'enseignement/contact.html', context)