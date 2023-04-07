from django.contrib import admin
from pharma.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Stock)
admin.site.register(Groupe)

@admin.register(Pharmacie)
class PharmacieAdmin(ImportExportModelAdmin):
    list_display = ('utilisateur', 'designation', 'latitude', 'longitude', 'adresse', 'telephone', 'ville', 'date_ajout', 'date_modif', 'groupe')

@admin.register(Produit)
class ProduitAdmin(ImportExportModelAdmin):
    list_display = ('designation', 'date_ajout', 'date_modif')

@admin.register(TourGarde)
class TourGardeAdmin(ImportExportModelAdmin):
    list_display = ('debut_tour', 'fin_tour', 'groupe')
