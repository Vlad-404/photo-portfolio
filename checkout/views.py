from django.shortcuts import render, redirect, reverse
from django.contrib import messages
<<<<<<< HEAD
=======
from django.conf import settings
>>>>>>> 0a0d9c695a10f1b9bc806458fe9701e685b0e93a
from home.models import Categories, SocialMedia

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()

media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart...")
        return redirect(reverse('image_presentation'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing!')

    template = 'checkout/checkout.html'
    context = {
        'page_title': 'Order Form',
        'media_links': media_links,
        'categories': all_categories,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
