from django.contrib import admin

# Register your models here.
from .models import User, Student, Enseignant, Tuteur


admin.site.register(Student)
admin.site.register(Enseignant)
admin.site.register(Tuteur)
admin.site.register(User)