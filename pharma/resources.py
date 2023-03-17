from import_export import resources
from .models import Produit

class ProduitResource(resources.ModelResource):
    class meta:
        model = Produit