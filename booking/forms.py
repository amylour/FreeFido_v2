from django import forms
from .models import Booking
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class BookingForm(forms.ModelForm):
    """ A form to create a booking """
    date = forms.DateField(widget=DatePickerInput(format="%Y-%m-%d"))
    time = forms.TimeField(widget=TimePickerInput(format="%H:%M"))

    class Meta:
        model = Booking
        fields = ['dog_name', 'breed', 'color',
                  'is_vaccinated', 'gender', 'date', 'time']
