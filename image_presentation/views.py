from django.shortcuts import render
from .models import Images
from home.models import SocialMedia

""" Social media links for navbar """
media_links = SocialMedia.objects.all()


# Create your views here.
# Galleries display
def all_images(request):
    """ A view that randomises the images each time page is loaded """
    random_list = Images.objects.order_by('?')
    context = {
        'media_links': media_links,
        'page_title': 'Galleries',
        'random': random_list
    }

    return render(request, 'gallery/gallery.html', context)


# More info for selected image
def image_view(request):
    """ A view that shows more info on an image and purchasing options """
    context = {
        'page_title': 'More info'
    }

    return render(request, 'gallery/image-view.html', context)
