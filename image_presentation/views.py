import random
from django.shortcuts import render
from .models import Images


# Create your views here.
def all_images(request):
    """ A view to show all of the images """
    images = Images.objects.all()
    random_list1 = Images.objects.order_by('?')
    random_list2 = Images.objects.order_by('?')
    random_list3 = Images.objects.order_by('?')
    context = {
        'images': images,
        'random1': random_list1,
        'random2': random_list2,
        'random3': random_list3,
    }

    return render(request, 'gallery/gallery.html', context)
