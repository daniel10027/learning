#######################################################################################################################################################
#######################################################################################################################################################
from django.contrib import admin
from .models import Recrutement, DossierRecrutement, Certificat, Diplome, Jury, Resultat
# Register your models here.

#######################################################################################################################################################
#######################################################################################################################################################
@admin.register(Recrutement)
class RecrutementAdmin(admin.ModelAdmin):
    search_fields = ['intitule']
    list_display  = ('intitule','ouverture','fermeture','date_debut_passage','date_fin_passage','resultat')
#######################################################################################################################################################
#######################################################################################################################################################
class CertificatInline(admin.TabularInline):
    model = Certificat
    extra = 0

class DiplomeInline(admin.TabularInline):
    model = Diplome
    extra = 0

@admin.register(DossierRecrutement)
class DossierAdmin(admin.ModelAdmin):
    inlines = [CertificatInline, DiplomeInline]
    search_fields = ['nom']
    list_display= ('recrutement','nom','prenom','localite','email','_diplome','_certificat','contact','status')
    def _diplome(self,obj):
         return obj.diplome.all().count()
    def _certificat(self,obj):
         return obj.certificat.all().count()

    
#######################################################################################################################################################
#######################################################################################################################################################
@admin.register(Jury)
class JuryAdmin(admin.ModelAdmin):
    '''Admin View for Jury'''
   
    list_display = ('recrutement','status')
    search_fields = ['nom']
#######################################################################################################################################################
#######################################################################################################################################################
@admin.register(Resultat)
class JuryAdmin(admin.ModelAdmin):
    '''Admin View for Jury'''
   
    list_display = ('dossier','juge','critere1','critere2','critere3','critere4','critere5')
    search_fields = ['dossier']
#######################################################################################################################################################
#######################################################################################################################################################
admin.site.register(Diplome)
admin.site.register(Certificat)