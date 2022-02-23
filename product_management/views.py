from audioop import reverse
from django.shortcuts import redirect, render, reverse
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