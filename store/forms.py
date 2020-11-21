from django import forms
from django.contrib.auth.forms import BillingForm
from django.contrib.auth.models import User


class AddressForm(BillingForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Valid email address required.')
    address = forms.CharField(max_length=75, required=True, help_text='Required.')
    city = forms.CharField(max_length=75, required=True, help_text='Required')
    state = forms.CharField(max_length=2, required=True, help_text='ex. NE')
    zip = forms.CharField(max_length=5, required=True, help_text='ex. 68124')

class PaymentForm(BillingForm):
    full_name = forms.CharField(max_length=50, required=True, help_text='Required.')
    method_number = forms.CharField(max_length=19, required=True, help_text='ex. 1111-2222-3333-4444.')
    exp_month = forms.CharField(max_length=9, required=True, help_text='ex. September.')
    exp_year = forms.CharField(max_length=4, required=True, help_text='ex. 2020.')
    cvv = forms.CharField(max_length=3, required=True, help_text='ex. 111')
