from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """ A form to create a booking """
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), input_formats=['%Y-%m-%d'])
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), input_formats=['%H:%M'])

    class Meta:
        model = Booking
        fields = ['user', 'email', 'dog_name', 'breed', 'color',
                  'is_vaccinated', 'gender', 'date', 'time']
