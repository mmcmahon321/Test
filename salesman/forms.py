from django import forms
from .models import Products, Customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', 'SKU', 'price', 'weight', 'product_description', 'product_category', 'product_stock', 'product_location', 'created_date', 'product_updated', 'image')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name', 'organization', 'role', 'account_number', 'address',
                  'city', 'state', 'zipcode', 'email', 'phone_number')