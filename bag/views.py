from django.shortcuts import redirect, render, reverse


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if cart[item_id] < 1:
        del cart[item_id]
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse('view-bag'))


def delete_item(request, item_id):
    cart = request.session.get('cart', {})

    del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('view-bag'))
