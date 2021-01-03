# Basic imports
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages

from django.conf import settings

# Imports models from other apps
from home.models import Categories, SocialMedia
from image_presentation.models import Images
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

# View specific imports
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents

import stripe
import json

# Defines variables for navbars and footer
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()

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
            order = order_form.save(commit=False)
            # gets the pid from Stripe payment intent
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            # adds the cart to the model for future use(purchase history)
            order.original_cart = json.dumps(cart)
            order.save()
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

        # Attempt to prefill the form with any info
        # the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    # If there's no Stripe key
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

    # If user is logged in
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the users info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your order was successfull! \
                     Your order number is {order_number}. \
                     A confirmation email will be sent to: {order.email}')

    # Deletes the cart after succesfull checkout
    if 'cart' in request.session:
        del request.session['cart']

    # builds the view
    template = 'checkout/checkout_success.html'
    context = {
        'page_title': 'Thank you!',
        'media_links': media_links,
        'categories': all_categories,
        'order': order,
    }
    messages.success(request,
                     f'Your purchase was successfull!'
                     )

    return render(request, template, context)
