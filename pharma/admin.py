from django.contrib import admin
from pharma.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Pharmacie)
admin.site.register(Stock)
admin.site.register(Groupe)
admin.site.register(Unite)
admin.site.register(PaysVille)
admin.site.register(Commande)

@admin.register(PharmacieGarde)
class PharmacieGardeAdmin(ImportExportModelAdmin):
    list_display = ('pharmacie', 'latitude', 'longitude', 'groupe')

@admin.register(Produit)
class ProduitAdmin(ImportExportModelAdmin):
    list_display = ('designation', 'date_ajout', 'date_modif')

@admin.register(TourGarde)
class TourGardeAdmin(ImportExportModelAdmin):
    list_display = ('debut_tour', 'fin_tour', 'groupe')

@admin.register(TourGardeCom5)
class TourGardeCom5Admin(ImportExportModelAdmin):
    list_display = ('debut_tour', 'fin_tour', 'groupe')

