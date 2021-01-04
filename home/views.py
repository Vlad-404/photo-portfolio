from django.shortcuts import render
from django.contrib import messages
from .models import Categories, SocialMedia


# Create your views here.
def index(request):
    media_links = SocialMedia.objects.all()
    all_categories = Categories.objects.all()

    context = {
        'page_title': 'Welcome',
        'categories': all_categories,
        'media_links': media_links
    }

    # base index.html view
    return render(request, 'home/index.html', context)
