from django import forms
from django.contrib.auth.models import User
from .models import GalleryImage


class GalleryImageForm(forms.ModelForm):
    """ A form to upload an image to the gallery wall """
    class Meta:
        model = GalleryImage
        fields = ['photo', 'title', 'image_description']
        # add a hidden input widget for photo_by
        # https://docs.djangoproject.com/en/4.2/ref/forms/widgets/
        widgets = {
            'photo_by': forms.HiddenInput(),
        }
