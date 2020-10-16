from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'SKU', 'price', 'weight', 'product_description', 'product_category', 'product_stock', 'product_location', 'created_date', 'product_updated')