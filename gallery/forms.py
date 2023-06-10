from django import forms
from django.contrib.auth.models import User
from .models import GalleryImage

class GalleryImageForm(forms.ModelForm):
    """ A form to upload an image to the gallery wall """
    class Meta:
        model = GalleryImage
        fields = ['title', 'photo', 'image_description']
        widgets = {
            'photo_by': forms.HiddenInput(),  # add a hidden input widget for photo_by
        }


