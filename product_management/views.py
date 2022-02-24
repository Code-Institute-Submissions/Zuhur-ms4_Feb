from audioop import reverse
import django
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from merchandise.models import Merchandise
from merchandise.views import merchandise
from .forms import ProductForm
# Create your views here.


@login_required
def product_management(request):
    if request.user.is_superuser:
        return render(request, 'product_management/product_management.html')
    else:
        return redirect(reverse('merch'))


@login_required
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
    if request.user.is_superuser:
        return render(request, 'product_management/add_product.html', context)
    else:
        return redirect(reverse('merch'))
    


@login_required
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
    if request.user.is_superuser:
        return render(request, 'product_management/edit_product.html', context)
    else:
        return redirect(reverse('merch'))
    


@login_required
def delete_product(request, pk):
    merch = Merchandise.objects.get(id=pk)

    if request.method == 'POST':
        merch.delete()
        return redirect(reverse('merch'))

    context = {
        'product': merch,
    }
    if request.user.is_superuser:
        return render(request, 'product_management/edit_product.html', context)
    else:
        return redirect(reverse('merch'))
