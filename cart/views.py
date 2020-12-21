from django.shortcuts import render
from home.models import SocialMedia, Categories

""" Social media links and categories """
media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()

# Create your views here.
def view_cart(request):
    """ A view that shows users cart """
    context = {
        'page_title': 'Your cart',
        'media_links': media_links,
        'categories': all_categories
    }

    # base index.html view
    return render(request, 'cart/cart.html', context)
