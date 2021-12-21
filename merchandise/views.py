from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Merchandise


def merchandise(request):

    merchandise = Merchandise.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'

            merchandise = merchandise.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # First filter by category
            merchandise = merchandise.filter(category__name__in=categories)
            # Second filter by gender
            merchandise = merchandise.filter(gender__name__in=categories)

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
    merch = get_object_or_404(Merchandise, pk=merch_id)
    context = {
        'merch': merch,
    }
    return render(request, 'merchandise/merch_detail.html', context)
