import stripe
from django.shortcuts import redirect, render, reverse
from django.conf import settings
from .forms import OrderForm
from django.contrib import messages
from bag.contexts import bag_contents
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Theres nothing in your bag")
        return redirect(reverse('merch'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)