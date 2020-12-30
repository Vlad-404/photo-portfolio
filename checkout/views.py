# Basic imports
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

# Imports models from other apps
from home.models import Categories, SocialMedia
from image_presentation.models import Images

# View specific imports
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents

import stripe
import json

# Defines variables for navbars and footer
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()


# Saves the info if customer selected to save the form info
@require_POST
def cache_checkout_data(request):
    try:
        # Stores the payment intent ID
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Sets up Stripe with the secret key so we can modify payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Now we modify the metadata
        stripe.PaymentIntent.modify(pid, metadata={
                # Gets the cart content and dumps it as json file
                'cart': json.dumps(request.session.get('cart', {})),
                # Gets the info if user wants to save form info or not
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            })
        return HttpResponse(status=200)
    except Exception as e:
        # In case of bad request, displays an error
        messages.error(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        return HttpResponse(content=e, status=400)


# Handles the payment process
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Gets the items from the cart
    cart = request.session.get('cart', {})

    # When submitting data with POST method...
    if request.method == 'POST':
        # Prepares the data
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Defines the varible that will be processed
        order_form = OrderForm(form_data)
        # If it's valid...
        if order_form.is_valid():
            order = order_form.save()
            # iterates through cart items and takes item_id and item_data
            for item_id, item_data in cart.items():
                # creates the order and saves it
                try:
                    if isinstance(item_data, int):
                        image = Images.objects.get(id=item_id)
                        order_line_item = OrderLineItem(
                            order=order,
                            image=image,
                            quantity=item_data,
                        )
                        order_line_item.save()
                # If for some reason image doesn't exist in db,
                # displays an error message and deletes the order
                except Images.DoesNotExist:
                    messages.error(request, (
                        "One of the images in your cart wasn't "
                        "found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # stores info from save-info from POST request into session
            request.session['save_info'] = 'save-info' in request.POST
            # and in the end, redirects to checkout_success page
            return redirect(reverse(
                                    'checkout_success',
                                    args=[order.order_number])
                            )
        # ... otherwise, if form isn't valid, displays an error message
        else:
            messages.error(request,
                           'There was an error with the information you provided. \
                           Please check if your information is correct.'
                           )
    # ...otherwise, if there's no POST method
    else:
        # Error handling if there's no cart, displays an error message
        # and sends the user back to galleries
        if not cart:
            messages.error(request, "There is nothing in your cart...")
            return redirect(reverse('image_presentation'))

        # defines the view with variables that
        # have been handled from another view
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        # Creates a payment intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    # Self explanatory
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing!')

    # builds the view
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


# Defines the view for successfull checkout
def checkout_success(request, order_number):
    # If checkout was succesfull
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order was successfull! \
                     Your order number is {order_number}. \
                     Check your messages for more details \
                     at the the email you provided: {order.email}')

    # Deletes the cart after succesfull checkout
    if 'cart' in request.session:
        del request.session['cart']

    # builds the view
    template = 'checkout/checkout_success.html'
    context = {
        'page_title': 'Thank you!',
        'order': order,
    }
    messages.success(request,
                     f'Your purchase was successfull!'
                     )

    return render(request, template, context)
