from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Imports models from other apps
from home.models import Categories, SocialMedia
from .models import UserProfile
from.forms import UserProfileForm


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
