from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Imports models from other apps
from home.models import Categories, SocialMedia

# Defines variables for navbars and footer
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()


# Displays the user's profile
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'

    context = {
        'page_title': 'Your Profile',
        'media_links': media_links,
        'categories': all_categories,
        'profile': profile,
    }

    return render(request, template, context)
