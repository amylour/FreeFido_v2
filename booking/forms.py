from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
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
        self.fields['date'].required = True
        

        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['color'].label = "Dog Color"
        self.fields['dog_name'].label = "Dog Name"
        self.fields['breed'].label = "Dog Breed"
        self.fields['gender'].label = "Dog Gender"

        self.fields['dog_name2'].label = "Second Dog Name"
        self.fields['breed2'].label = "Second Dog Breed"
        self.fields['color2'].label = "Secong Dog Color"
        self.fields['is_vaccinated2'].label = "Is vaccinated?"
        self.fields['gender2'].label = "Second Dog Gender"

        self.fields['is_vaccinated2'].widget = forms.CheckboxInput()

        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

        def form_valid(self, form):
            form.instance.user = self.request.user

            # Check if a booking with the same date and time already exists
            if Booking.objects.filter(date=form.instance.date, time=form.instance.time).exists():
                messages.error(
                    self.request, 'This date and time is already booked.')
                return self.form_invalid(form)

            messages.success(self.request, 'Your booking has been saved.')
            return super().form_valid(form)

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'dog_name', 'breed', 'color',
                  'is_vaccinated', 'gender', 'date', 'time', 'dog_name2', 'breed2', 'color2', 'is_vaccinated2', 'gender2']
        unique_together = ['date', 'time']
