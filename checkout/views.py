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
        'stripe_public_key': 'pk_test_51K8oHhHRpFGpRYkNxy58BLsBf5YM5hBZ6KD7UNSUIh3eVWkGTy8Zz3fML1CRTOpgB5KH7P2Dq6J622ljSTUMPZ6z00aFjIbtzd',
        'client_secret': 'some secret'
    }
    return render(request, 'checkout/checkout.html', context)