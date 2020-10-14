from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', 'SKU', 'price', 'weight', 'product_description', 'product_category', 'product_stock', 'product_location', 'product_added', 'product_updated')