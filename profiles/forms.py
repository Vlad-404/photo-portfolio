from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # Defines the placeholders for the form
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        # Sets the cursor in the Name field by default
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Changes the values for  for each form field
        for field in self.fields:
            # As country field is handled by CountryField,
            # I don't have it in placeholders.
            # This if statement is handling the error that
            # would be caused by if statement content
            if field != 'default_country':
                # Adds asterisk if field is required
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Changes the placeholder values
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Adds css class of 'stripe-style-input'
            self.fields[field].widget.attrs['class'] = 'border-black rounded-1'
            # Removes the default form field labels
            self.fields[field].label = False
