import django_filters

from django_filters import CharFilter
from .models import *

class StockFilter(django_filters.FilterSet):
    produit = CharFilter(field_name='produit', lookup_expr='icontains')
    class Meta:
        model = Stock
        fields = ['produit']