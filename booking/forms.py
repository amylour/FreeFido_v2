from django import forms
from django.contrib.auth.models import User
from .models import Booking


class BookingForm(forms.ModelForm):
    """ A form to create a booking """

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'dog_name', 'breed', 'color',
                  'is_vaccinated', 'gender', 'date', 'time']
