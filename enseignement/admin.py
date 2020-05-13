from django.contrib import admin
from django.utils.safestring import mark_safe
from configuration.admin import Pass_true, Pass_false
from .models import (Localite,
                     TypeEtablissement,
                     StatutEtablissement,
                     Etablissement,
                     DominaceUfr,
                     Ufr,
                     Filiere,
                     Specialite,
                     Niveau,
                     Semestre,
                     TypeUe,
                     UniteEnseignement,
                     Ecue,
                     Cours,
                     RessourcePdf,
                     RessourceVideo)
#############################################
class PdfInline(admin.TabularInline):
    model = RessourcePdf
    extra = 0

class VideoInline(admin.TabularInline):
    model = RessourceVideo
    extra = 0

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
   
    inlines = [PdfInline, VideoInline]
    search_fields = ['intitule']
    readonly_fields = ["images"]
    actions = [Pass_true, Pass_false]
    def images(self, obj):
        return mark_safe('<img src="{url}" style="width: 45px; height:45px;" />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )
    list_display = ('images','intitule','ecue','status','_pdf','_video')
    def _pdf(self, obj):
        return obj.ressourcepdf.all().count()
    def _video(self, obj):
        return obj.ressourcevideo.all().count()
#################################################################
class UfrInline(admin.TabularInline):
    model = Ufr
    extra = 0
@admin.register(Etablissement)
class EtabAdmin(admin.ModelAdmin):
    search_fields = ['nom']
    inlines = [UfrInline]
    actions = [Pass_true, Pass_false]
    list_display= ('nom','localite','adresse','type_etablissement','statut_etablissement','_ufr','directeur_general','status')
    def _ufr(self, obj):
        return obj.etablissement_ufr.all().count()
#################################################################
class SpecialiteInline(admin.TabularInline):
    model = Specialite
    extra = 0
@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    inlines = [SpecialiteInline]
    search_fields = ['nom']
    list_display= ('nom','departement','_specialite','status','created','date_update')
    actions = [Pass_true, Pass_false]
    def _specialite(self, obj):
        return obj.specialite_filiere.all().count()
#################################################################
class EcueInline(admin.TabularInline):
    model = Ecue
    extra = 0
@admin.register(UniteEnseignement)
class UeAdmin(admin.ModelAdmin):
    inlines= [EcueInline]
    search_fields = ['nom']
    actions = [Pass_true, Pass_false]
    list_display= ('nom','specialite','type','niveau','semestre','_ecue','status')
    def _ecue(self,obj):
         return obj.ecue_ue.all().count()

class ecadmin(admin.ModelAdmin):
    readonly_fields = ["images"]
    actions = [Pass_true, Pass_false]
    def images(self, obj):
        return mark_safe('<img src="{url}" style="width: 45px; height:45px;" />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
    )
    list_display= ('images','intitule','ue','enseignant','credit','status')
#############################################################################
# Register your models here.
class LocaliteAdmin(admin.ModelAdmin):
    search_fields = ['nom']
    list_display= ('nom','status','created','date_update')
    actions = [Pass_true, Pass_false]
    
class NiveauAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class SemestreAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class TypeUeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
   
class TypeEtabAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class StatutEtabAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class DominanceAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class UfrAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class SpecialiteAdmin(admin.ModelAdmin):
   def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(Localite, LocaliteAdmin)
admin.site.register(TypeEtablissement, TypeEtabAdmin)
admin.site.register(StatutEtablissement, StatutEtabAdmin)

admin.site.register(DominaceUfr, DominanceAdmin)
admin.site.register(Ufr, UfrAdmin)

admin.site.register(Specialite, SpecialiteAdmin)
admin.site.register(Niveau, NiveauAdmin)
admin.site.register(Semestre, SemestreAdmin)
admin.site.register(TypeUe, TypeUeAdmin)
