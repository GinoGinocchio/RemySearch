from django.contrib import admin
from .models import *
# Register your models here.

class ArchivoPDFAdmin(admin.ModelAdmin):
    list_display = ['id', 'archivo']
    search_fields = ['id']

admin.site.register(ArchivoPDF, ArchivoPDFAdmin)