from django import forms
from .models import Images
from .widgets import CustomClearableFileInput


class ImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = '__all__'

    image = forms.ImageField(
                label='Image',
                required=False,
                widget=CustomClearableFileInput
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1 osans'
