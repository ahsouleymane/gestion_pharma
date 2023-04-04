from import_export import resources
from .models import Produit, TourGarde

class ProduitResource(resources.ModelResource):
    class meta:
        model = Produit

class TourGardeResource(resources.ModelResource):
    class meta:
        model = TourGarde