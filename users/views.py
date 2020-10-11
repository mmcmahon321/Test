from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm


# Create your views here.

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(response, user)
		return redirect("/home")
	else:
		form = RegisterForm()

	return render(response, "users/register.html", {"form":form})