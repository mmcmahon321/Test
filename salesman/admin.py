from django.contrib import admin

from .models import Products

class ProductList(admin.ModelAdmin):
    list_display = ('product_name', )
    list_filter = ('product_name', )
    search_fields = ('product_name', )


admin.site.register(Products, ProductList)