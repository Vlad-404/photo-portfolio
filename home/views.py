from django.shortcuts import render
from .models import categories, SocialMedia


# Create your views here.
def index(request):
    media_links = SocialMedia.objects.all()
    category = categories.objects.all()
    context = {
        'categories': category,
        'media_links': media_links
    }

    # base index.html view
    return render(request, 'home/index.html', context)
