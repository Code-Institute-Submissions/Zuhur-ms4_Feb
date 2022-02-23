from audioop import reverse
from django.shortcuts import redirect, render, reverse
from merchandise.models import Merchandise

from merchandise.views import merchandise
from .forms import ProductForm
# Create your views here.

def product_management(request):
    return render(request, 'product_management/product_management.html')

def add_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('merch'))

    context = {
        'form': form
    }
    return render(request, 'product_management/add_product.html', context)


def edit_product(request, pk):
    merch = Merchandise.objects.get(id=pk)
    form = ProductForm(instance=merch)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=merch)
        if form.is_valid():
            form.save()
            return redirect(reverse('merch'))
    context = {
        'form': form
    }
    return render(request, 'product_management/edit_product.html', context)