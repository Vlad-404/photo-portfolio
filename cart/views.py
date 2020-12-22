from django.shortcuts import render, redirect
from home.models import SocialMedia, Categories

""" Social media links and categories """
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()

# Create your views here.
def view_cart(request):
    """ A view that shows users cart """
    context = {
        'page_title': 'Your cart',
        'media_links': media_links,
        'categories': all_categories
    }

    # base index.html view
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
    print(request.session['cart'])
    return redirect(redirect_url)
