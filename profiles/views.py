from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Imports models from other apps
from home.models import Categories, SocialMedia
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


# Defines variables for navbars and footer
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()


# Displays the user's profile
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all(

    )
    template = 'profiles/profile.html'
    context = {
        'page_title': 'Your Profile',
        'media_links': media_links,
        'categories': all_categories,
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
        f'This a confirmation for your previous order number: {order_number}'
        'A confirmation email was sent on the order date.'
        ))

    template = 'checkout/checkout_success.html'
    context = {
        'page_title': 'Order History',
        'media_links': media_links,
        'categories': all_categories,
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
