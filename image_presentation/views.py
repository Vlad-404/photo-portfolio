from django.shortcuts import render
from .models import Images
from home.models import SocialMedia


# Create your views here.
def all_images(request):
    """ Import social media links for navbar """
    media_links = SocialMedia.objects.all()

    """ A view that randomises the images each time page is loaded """
    random_list = Images.objects.order_by('?')
    context = {
        'media_links': media_links,
        'page_title': 'Galleries',
        'random': random_list
    }

    return render(request, 'gallery/gallery.html', context)
