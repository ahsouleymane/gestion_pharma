from django.contrib import admin
from pharma.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Pharmacie)
admin.site.register(Stock)

@admin.register(Produit)
class ProduitAdmin(ImportExportModelAdmin):
    list_display = ('designation', 'date_ajout', 'date_modif')