from django.shortcuts import get_object_or_404, render
from .models import Merchandise

# Create your views here.
def merchandise(request):
    merchandise = Merchandise.objects.all()
    context = {
        'merchandise': merchandise,
    }
    return render(request, 'merchandise/merch.html', context)


def merchandise_detail(request, merch_id):
    merch = get_object_or_404(Merchandise, pk=merch_id)
    context = {
        'merch': merch,
    }
    return render(request, 'merchandise/merch_detail.html', context)