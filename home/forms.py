from django import forms


class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True)
    contact_message = forms.TextInput(required=True)
