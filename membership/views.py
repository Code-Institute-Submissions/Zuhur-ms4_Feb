from django.shortcuts import render


def membership(request):
    return render(request, 'membership/membership.html')
