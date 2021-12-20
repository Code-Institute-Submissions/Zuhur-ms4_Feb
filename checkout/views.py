import stripe
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from bag.contexts import bag_contents
from merchandise.models import Merchandise
from .models import Order, OrderLineItem
from .forms import OrderForm

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'town_or_city': request.POST['town_or_city'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in cart.items():
                merch = Merchandise.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order = order,
                    merch = merch,
                    quantity = quantity,
                )
                order_line_item.save()
            request.session['save_details'] = 'save-details' in request.POST
            
            return redirect(reverse('checkout-success', args=[order.order_number]))

    else:
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


def checkout_success(request, order_number):
    save_details = request.session.get('save_details')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successful! Your order number is {order_number}')

    if 'cart' in request.session:
        del request.session['cart']
    
    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)


