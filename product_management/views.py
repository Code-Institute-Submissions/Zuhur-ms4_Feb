from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

def product_management(request):
    return render(request, 'product_management/product_management.html')
