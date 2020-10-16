from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import redirect


now = timezone.now()

@login_required
def product_list(request):
    product = Product.objects.filter(product_updated__lte=timezone.now())
    return render(request, 'salesman_product_page.html',
                  {'product': product})

@login_required
def product_edit(request, pk):
   product = get_object_or_404(Product, pk=pk)
   if request.method == "POST":
       # update
       form = ProductForm(request.POST, instance=product)
       if form.is_valid():
           product = form.save()
           product.updated_date = timezone.now()
           product.save()
           product = Product.objects.filter(created_date__lte=timezone.now())
           return render(request, 'salesman_product_page.html',
                         {'product': product})
   else:
        # edit
       form = ProductForm(instance=product)
   return render(request, 'salesman_product_edit.html', {'form': form})

def product_delete(request, pk):
   product = get_object_or_404(Product, pk=pk)
   product.delete()
   return redirect('salesman:product_list')

@login_required
def product_new(request):
   if request.method == "POST":
       form = ProductForm(request.POST)
       if form.is_valid():
           product = form.save(commit=False)
           product.created_date = timezone.now()
           product.save()
           product = Product.objects.filter(created_date__lte=timezone.now())
           return render(request, 'salesman_product_page.html',
                         {'product': product})
   else:
       form = ProductForm()
       # print("Else")
   return render(request, 'salesman_product_new.html', {'form': form})

