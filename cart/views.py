from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from home.models import SocialMedia, Categories
from django.contrib import messages

from image_presentation.models import Images

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

    image = get_object_or_404(Images, pk=image_id)
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if image_id in list(cart.keys()):
        cart[image_id] += quantity
        messages.success(request,
                         f'Quantity for "{image.title}" image has been updated')
    else:
        cart[image_id] = quantity
        messages.success(request,
                         f'You have successfully added "{image.title}" to your cart. Click the cart icon above to see your cart.')

    request.session['cart'] = cart
    return redirect('all_images')


def adjust_cart(request, image_id):
    """Adjust the quantity of the specific image added to cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    image = get_object_or_404(Images, pk=image_id)

    if quantity > 0:
        cart[image_id] = quantity
        messages.success(request,
                         f'Quantity for "{image.title}" image has been updated')
        if quantity > 5:
            quantity = 5
    else:
        cart.pop(image_id)
        messages.success(request,
                         f'You have removed "{image.title}" from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, image_id):
    """ Removes the item from shopping cart """
    try:
        image = get_object_or_404(Images, pk=image_id)
        cart = request.session.get('cart', {})
        cart.pop(image_id)
        messages.success(request,
                         f'You have removed "{image.title}" from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing image: {e}')
        return HttpResponse(status=500)
