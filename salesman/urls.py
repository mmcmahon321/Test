from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'salesman'
urlpatterns = [
    path('salesman_product_page', views.product_list, name='product_list'),
    path('salesman_customer_list', views.customer_list, name='customer_list'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/create/', views.product_new, name='product_new'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('product/product_search/', views.product_search, name='product_search'),
]