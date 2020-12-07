from django.shortcuts import render
from .models import Images


# Create your views here.
def all_images(request):
    """ A view to show all of the images """
    images = Images.objects.all()
    context = {
        'images': images,
    }

    return render(request, 'gallery/gallery.html', context)
