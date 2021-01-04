from django.shortcuts import render
from .models import Categories, SocialMedia
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    media_links = SocialMedia.objects.all()
    all_categories = Categories.objects.all()

    # if user uses contact form
    if request.method == 'POST':
        my_email = settings.DEFAULT_FROM_EMAIL
        # gets the data
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_message = request.POST['contact-message']

        # Handles sending of confirmation emails
        subject = render_to_string(
            'home/contact_emails/contact_email_subject.txt',
            {'contact_name': contact_name})
        body = render_to_string(
            'home/contact_emails/contact_email_body.txt',
            {
             'contact_email': contact_email,
             'contact_message': contact_message,
             'contact_name': contact_name
            })

        send_mail(
            subject,
            body,
            contact_email,
            [my_email]
        )

        # displays confirmation message and renders the page
        messages.success(request, (
                        f'Thank you {contact_name}. Your message was sent succesfully \
                        and will be answered as soon as possible'))
        context = {
            'page_title': 'Welcome',
            'categories': all_categories,
            'media_links': media_links,
            'contact_name': contact_name
        }
        return render(request, 'home/index.html', context)

    else:
        context = {
            'page_title': 'Welcome',
            'categories': all_categories,
            'media_links': media_links
        }

        # base index.html view
        return render(request, 'home/index.html', context)
