from django.shortcuts import render
from .models import Merchandise

# Create your views here.
def merchandise(request):
    merchandise = Merchandise.objects.all()
    context = {
        'merchandise': merchandise,
    }
    return render(request, 'merchandise/merch.html', context)
    