from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Images
from home.models import SocialMedia, categories

""" Social media links for navbar """
media_links = SocialMedia.objects.all()
categories = categories.objects.all()


# Galleries display
def all_images(request):
    """ A view that randomises the images each time page is loaded """
    random_list = Images.objects.order_by('?')
    images = Images.objects.all()
    query = None
    # category = None

    """ This part handles the search query """
    if request.GET:
        # if 'category' in request.GET:
        #    sort_by_category = request.GET['category']
        #    random_list = images.filter(category__name__in=categories)
        #    sort_by_category = categories.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Your search query is empty. Please enter a search term if you wish to use search.")
                return redirect(reverse('all_images'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            random_list = images.filter(queries)

    context = {
        'media_links': media_links,
        'categories': categories,
        'page_title': 'Galleries',
        'random': random_list,
        # 'sort_by_category': sort_by_category,
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
