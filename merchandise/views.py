from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Merchandise

# Create your views here.
def merchandise(request):


    merchandise = Merchandise.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Enter into search bar for a result")
                return redirect(reverse('merch'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            merchandise = merchandise.filter(queries)

    context = {
        'merchandise': merchandise,
        'search_query': query,
    }
    return render(request, 'merchandise/merch.html', context)


def merchandise_detail(request, merch_id):
    merch = get_object_or_404(Merchandise, merch_id)
    context = {
        'merch': merch,
    }
    return render(request, 'merchandise/merch_detail.html', context)