from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100, required=True)
    password2 = forms.CharField(label="Password confirmation", help_text="")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]