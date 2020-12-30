from django.http import HttpResponse


# Handles Stripe webhooks
class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    # Handles generic/unexpected/unknown webhook event(s)
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unknown webhook received: {event["type"]}',
            status=200)

    # Handles successfull payment process webhook from Stripe
    def handle_payment_intent_succeeded(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Handles failed payment process webhook from Stripe
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)