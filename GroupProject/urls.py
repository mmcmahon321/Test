"""GroupProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,  include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from users import views as u
from contact import views as c
from store import views as s
from salesman import views as sm



urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('register/', u.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout/completed'), name='logout'),
    path('logoutsuccessful/', TemplateView.as_view(template_name='users/logoutsuccessful.html'), name='logoutsuccessful'),
    path("about/", TemplateView.as_view(template_name='about.html'), name='about'),
    path("contact/", c.contact, name="contact"),
    path("contact/success/", TemplateView.as_view(template_name='contact/success.html'), name='success'),
    path("payment", s.payment, name="payment"),
    path("store/", s.store, name="store"),
    path("cart/", s.cart, name="cart"),
    path("checkout/", s.checkout, name="checkout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('change_password/', u.change_password, name='change_password'),
    path('password_updated/', u.password_updated, name='password_updated'),
    path('salesman_product_page', sm.product_list, name='product_list'),
    path('salesman_customer_list', sm.customer_list, name='customer_list'),
    path('product/<int:pk>/delete/', sm.product_delete, name='product_delete'),
    path('product/<int:pk>/edit/', sm.product_edit, name='product_edit'),
    path('product/create/', sm.product_new, name='product_new'),
    path('customer/create/', sm.customer_new, name='customer_new'),
    path('customer/<int:pk>/edit/', sm.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', sm.customer_delete, name='customer_delete'),
    path('product/product_search/', sm.product_search, name='product_search'),
]
