from .models import Products, Customer
import django_filters


class Product_filters(django_filters.FilterSet):
    product_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Products
        fields = ['product_name', 'SKU', ]


class Customer_filters(django_filters.FilterSet):
    cust_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = ['account_number', 'cust_name', 'email','phone_number']
