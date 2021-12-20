from django.shortcuts import get_object_or_404
from merchandise.models import Merchandise
from decimal import Decimal


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    cart = request.session.get('cart', {})
    for item_id, quantity in cart.items():
        merch = get_object_or_404(Merchandise, pk=item_id)
        total += Decimal(quantity * merch.price)
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'merch': merch,
        })
    delivery = Decimal(4.99)
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    print(grand_total)
    return context 