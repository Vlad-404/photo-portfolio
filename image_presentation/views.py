from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Images
from home.models import SocialMedia, categories

""" Social media links for navbar """
media_links = SocialMedia.objects.all()
all_categories = categories.objects.all()


# Galleries display
def all_images(request):
    """ A view that randomises the images each time page is loaded """
    random_list = Images.objects.order_by('?')
    images = Images.objects.all()
    query = None
    category_sort = None

    if request.GET:
        """ This part handles sorting by name, rating and price """
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey == 'name':
                sortkey = 'lower_name'
                random_list = images.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            random_list = images.order_by(sortkey)

        """ This part displays only panorama images """
        if 'panorama' in request.GET:
            random_list = Images.objects.filter(panorama=True)

        """ This part displays only black and white images """
        if 'color' in request.GET:
            random_list = Images.objects.filter(color=False)

        """ This part handles category sorting """
        if 'category' in request.GET:
            category_sort = request.GET['category']
            random_list = Images.objects.filter(category__name=category_sort)

        """ This part show all panoramas for selected category """
        if 'category_panorama' in request.GET:
            category_panorama = request.GET['category_panorama']
            random_list = Images.objects.filter(
                            category__name=category_panorama
                            ).filter(
                            panorama=True
                            )

        """ This part show all black and white images for selected category """
        if 'category_color' in request.GET:
            category_color = request.GET['category_color']
            random_list = Images.objects.filter(
                            category__name=category_color
                            ).filter(
                            color=False
                            )

        all_queries = ('panorama',
                        'color',
                        'category',
                        'category_panorama',
                        'category_color'
                        )
        if request.GET not in all_queries:
            messages.info(
                        request,
                        "Sorry, there are no results for this query."
                        )

        """ This part handles the search query """
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Your search query is empty. Please enter a search term if you wish to use search.")
                return redirect(reverse('all_images'))

            queries = Q(
                title__icontains=query
                ) | Q(
                description__icontains=query
                )
            random_list = images.filter(queries)

    context = {
        'media_links': media_links,
        'categories': all_categories,
        'page_title': 'Galleries',
        'random': random_list,
        'category_sort': category_sort,
    }

    return render(request, 'gallery/gallery.html', context)


# More info for selected image
# def image_view(request, image_id):
def image_view(request, image_id):
    """ A view to show individual image details with purchasing options"""
    image = get_object_or_404(Images, pk=image_id)

    context = {
        'image': image,
        'categories': all_categories,
        'page_title': 'More info'
    }

    return render(request, 'gallery/image-view.html', context)
