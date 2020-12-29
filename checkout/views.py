from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart...")
        return redirect(reverse('image_presentation'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'page_title': 'Order Form',
        'order_form': order_form,
    }

    return render(request, template, context)
