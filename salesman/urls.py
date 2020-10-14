from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

app_name = 'salesman'
urlpatterns = [
    path('salesman_product_page', views.product_list, name='product_list')
]