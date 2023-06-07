from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Booking
from .forms import BookingForm


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    A view to create a booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_create.html'
    success_url = '/booking/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

