from django.shortcuts import render

# Imports models from other apps
from home.models import Categories, SocialMedia

# Defines variables for navbars and footer
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()


# Displays the user's profile
def profile(request):
    template = 'profiles/profile.html'
    context = {
        'page_title': 'Your Profile',
        'media_links': media_links,
        'categories': all_categories,
    }

    return render(request, template, context)
