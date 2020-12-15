from django.shortcuts import render
from .models import categories, SocialMedia


# Create your views here.
def index(request):
    media_links = SocialMedia.objects.all()
    all_categories = categories.objects.all()
    context = {
        'page_title': 'Welcome',
        'categories': all_categories,
        'media_links': media_links
    }

    # base index.html view
    return render(request, 'home/index.html', context)
