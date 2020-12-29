from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from home.models import Categories, SocialMedia

from .forms import OrderForm

media_links = SocialMedia.objects.all()
all_categories = Categories.objects.all()

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart...")
        return redirect(reverse('image_presentation'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'page_title': 'Order Form',
        'media_links': media_links,
        'categories': all_categories,
        'order_form': order_form,
    }

    return render(request, template, context)
