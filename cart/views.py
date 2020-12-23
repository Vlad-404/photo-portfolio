from django.shortcuts import render, redirect, reverse, HttpResponse
from home.models import SocialMedia, Categories

""" Social media links and categories """
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()


def view_cart(request):
    """ A view that shows users cart """
    context = {
        'page_title': 'Your cart',
        'media_links': media_links,
        'categories': all_categories
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, image_id):
    """ Add a number of specific image to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if image_id in list(cart.keys()):
        cart[image_id] += quantity
    else:
        cart[image_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specific image added to cart"""

    # image = get_object_or_404(Images, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    print(item_id)
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Removes the item from shopping cart """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
