from django.http import HttpResponse
from django.shortcuts import render


def home(response):
    return render(response, "home.html", {})
