from django.contrib import admin

# Register your models here.
from .models import User, Student, Enseignant, Tuteur, Grade,Domaine


admin.site.register(Student)
admin.site.register(Enseignant)
admin.site.register(Tuteur)
admin.site.register(User)
admin.site.register(Grade)
admin.site.register(Domaine)