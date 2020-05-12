from django.contrib import admin

# Register your models here.
from .models import Partenaire, CopyRight, ContactInfo

@admin.register(Partenaire)
class Pa(admin.ModelAdmin):
    search_fields = ['nom']
    list_display= ('nom','status','created','date_update')

@admin.register(CopyRight)
class Cp(admin.ModelAdmin):
    search_fields = ['nom']
    list_display= ('nom','status','created','date_update')

@admin.register(ContactInfo)
class Co(admin.ModelAdmin):
    search_fields = ['titre']
    list_display= ('titre','status','created','date_update')