from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """ form for user to create a profile """
    class Meta:
        model = Profile
        fields = ['image', 'display_name', 'bio']

        labels = {
            "image": "Profile Pic",
            "display_name": "Display Name",
            "bio": "Bio"

        }
