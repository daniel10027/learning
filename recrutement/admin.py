#######################################################################################################################################################
#######################################################################################################################################################
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Recrutement, DossierRecrutement, Certificat, Diplome, Jury, Resultat, MyModelAdmin, Critere
from configuration.admin import Pass_false,Pass_true
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

#######################################################################################################################################################
#######################################################################################################################################################
class CritereInline(admin.TabularInline):
    model = Critere
    extra = 0

@admin.register(Recrutement)
class RecrutementAdmin(admin.ModelAdmin):
    inlines = [CritereInline,]
    search_fields = ['intitule']
    list_display  = ('intitule','ouverture','fermeture','date_debut_passage','date_fin_passage','_critere','resultat')
    actions = [Pass_true, Pass_false]
    def _critere(self,obj):
         return obj.criteres.all().count()
#######################################################################################################################################################

#######################################################################################################################################################
class CertificatInline(admin.TabularInline):
    model = Certificat
    extra = 0
##########
class DiplomeInline(admin.TabularInline):
    model = Diplome
    extra = 0
class DocRessources(resources.ModelResource):
    class Meta:
        model = DossierRecrutement
        fields = ('id','recrutement','nom','prenom','localite','email','_diplome','_certificat','contact')
@admin.register(DossierRecrutement)
class DossierAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    inlines = [CertificatInline, DiplomeInline]
    resource_class = DocRessources
    search_fields = ['nom']
    list_display= ('recrutement','nom','prenom','localite','email','_diplome','_certificat','contact','status')
    def _diplome(self,obj):
         return obj.diplome.all().count()
    def _certificat(self,obj):
         return obj.certificat.all().count()

    
#######################################################################################################################################################
#######################################################################################################################################################
'''
@admin.register(Jury)
class JuryAdmin(admin.ModelAdmin):
    #Admin View for Jury
   
    list_display = ('recrutement','status')
    search_fields = ['nom']
    actions = [Pass_true, Pass_false]
'''
#######################################################################################################################################################
#######################################################################################################################################################
@admin.register(Resultat)
class JuryAdmin(admin.ModelAdmin):
    '''Admin View for Jury'''
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('dossier','juge','critere1','critere2','critere3','critere4','critere5')
    search_fields = ['dossier']
#######################################################################################################################################################
#######################################################################################################################################################
admin.site.register(Diplome)
admin.site.register(Certificat)
admin.site.register(Jury, MyModelAdmin)
#############################""