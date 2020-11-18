from django.contrib import admin
from .models import Products, Customer, Category


class ProductList(admin.ModelAdmin):
    list_display = ('product_name', )
    list_filter = ('product_name', )
    search_fields = ('product_name', )


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'organization', 'phone_number')
    list_filter = ('cust_name', 'organization')
    search_fields = ('cust_name',)
    ordering = ['cust_name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductList)
admin.site.register(Customer, CustomerList)