from django.shortcuts import render, get_object_or_404
from .models import Images
from home.models import SocialMedia, categories

""" Social media links for navbar """
media_links = SocialMedia.objects.all()
categories = categories.objects.all()


# Create your views here.
# Galleries display
def all_images(request):
    """ A view that randomises the images each time page is loaded """
    random_list = Images.objects.order_by('?')
    context = {
        'media_links': media_links,
        'categories': categories,
        'page_title': 'Galleries',
        'random': random_list
    }

    return render(request, 'gallery/gallery.html', context)


# More info for selected image
# def image_view(request, image_id):
def image_view(request, image_id):
    """ A view to show individual image details with purchasing options"""
    image = get_object_or_404(Images, pk=image_id)

    context = {
        'image': image,
        'page_title': 'More info'
    }

    return render(request, 'gallery/image-view.html', context)
