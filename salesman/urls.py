from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'salesman'
urlpatterns = [
    path('salesman_product_page', views.product_list, name='product_list'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/create/', views.product_new, name='product_new'),
]