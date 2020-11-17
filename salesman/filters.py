from .models import Products
import django_filters

class Product_filters(django_filters.FilterSet):
    product_name = django_filters.CharFilter
    class Meta:
        model = Products
        fields = [ 'product_name', 'SKU',]
