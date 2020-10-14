from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import redirect


now = timezone.now()

@login_required
def product_list(request):
    product = Products.objects.filter(product_updated__lte=timezone.now())
    return render(request, 'salesman_product_page.html',
                  {'product': product})