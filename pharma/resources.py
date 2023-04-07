from import_export import resources
from .models import Produit, TourGarde, Pharmacie

class ProduitResource(resources.ModelResource):
    class meta:
        model = Produit

class TourGardeResource(resources.ModelResource):
    class meta:
        model = TourGarde

class PharmacieResource(resources.ModelResource):
    class meta:
        model = Pharmacie
