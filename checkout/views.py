from django.shortcuts import redirect, render, reverse
from .forms import OrderForm
from django.contrib import messages
# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Theres nothing in your bag")
        return redirect(reverse('merch'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
    }
    return render(request, 'checkout/checkout.html', context)