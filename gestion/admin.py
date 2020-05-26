from django.contrib import admin

# Register your models here.
from .models import User, Student, Enseignant, Tuteur, Grade,Domaine,TypeEnseignant

class GradeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    
class DomaineAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
###############
class TypeA(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
    
class Ens(admin.ModelAdmin):
    list_display = ('user','matricule','type','structure','grade')  
admin.site.register(Student)
admin.site.register(Enseignant, Ens)
admin.site.register(Tuteur)
admin.site.register(User)
admin.site.register(Grade,GradeAdmin)
admin.site.register(Domaine,  DomaineAdmin)
admin.site.register(TypeEnseignant,  TypeA)