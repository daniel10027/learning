from django.contrib import admin

# Register your models here.
from .models import Partenaire, CopyRight, ContactInfo, Message

def Pass_true(ModelAdmin, request,queryset):
    queryset.update(status=True)
Pass_true.short_description = "Activer les elements sélectionnés"

def Pass_false(ModelAdmin, request,queryset):
    queryset.update(status=False)
Pass_false.short_description = "Désactiver les elements sélectionnés"
#########################
@admin.register(Partenaire)
class Pa(admin.ModelAdmin):
    search_fields = ['nom']
    list_display= ('nom','status','created','date_update')
    actions = [Pass_true, Pass_false]

@admin.register(CopyRight)
class Cp(admin.ModelAdmin):
    search_fields = ['nom']
    list_display= ('nom','status','created','date_update')

@admin.register(ContactInfo)
class Co(admin.ModelAdmin):
    search_fields = ['titre']
    list_display= ('titre','status','created','date_update')

@admin.register(Message)
class Co(admin.ModelAdmin):
    search_fields = ['titre']
    list_display= ('titre','description','status','created','date_update')