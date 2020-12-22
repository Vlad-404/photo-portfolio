from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from image_presentation.models import Images


def cart_contents(request):

    cart_items = []
    total = 0
    images_count = 0
    cart = request.session.get('cart', {})

    for image_id, quantity in cart.items():
        images = get_object_or_404(Images, pk=image_id)
        total += quantity * images.price
        images_count += quantity
        cart_items.append({
            'image_id': image_id,
            'quantity': quantity,
            'images': images
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'images_count': images_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context
