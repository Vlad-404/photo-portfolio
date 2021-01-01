from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # Defines the placeholders for the form
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Sets the cursor in the Name field by default
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Changes the values for  for each form field
        for field in self.fields:
            # As country field is handled by CountryField,
            # I don't have it in placeholders.
            # This if statement is handling the error that
            # would be caused by if statement content
            if field != 'country':
                # Adds asterisk if field is required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Changes the placeholder values
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Adds css class of 'stripe-style-input'
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Removes the default form field labels
            self.fields[field].label = False
