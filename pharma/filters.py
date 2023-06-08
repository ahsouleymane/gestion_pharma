import django_filters

from django_filters import CharFilter
from .models import *

class StockFilter(django_filters.FilterSet):
    class Meta:
        model = Stock
        fields = ['pharmacie', 'produit']