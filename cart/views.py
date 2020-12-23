from django.shortcuts import render, redirect, reverse
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


def add_to_cart(request, images_id):
    """ Add a number of specific image to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if images_id in list(cart.keys()):
        cart[images_id] += quantity
    else:
        cart[images_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request):
    """ Update quantity of images """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    # if quantity > 0:
    #     cart[images_id] = quantity
    # else:
    #     cart.pop[images_id]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
