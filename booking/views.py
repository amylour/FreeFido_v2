from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic, View
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from .models import Booking
from .forms import BookingForm

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    A view to create a booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_create.html'
    # Use the URL name of your booking success page
    success_url = reverse_lazy('booking_success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your booking has been saved.')
        return super().form_valid(form)


class ActiveBookings(LoginRequiredMixin, generic.ListView):
    """
    A view to display the user's bookings
    """
    model = Booking
    template_name = 'booking/booking_success.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        # Filter bookings based on the currently logged-in user
        return Booking.objects.filter(user=self.request.user).order_by('-date')


class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a booking """
    model = Booking
    success_url = reverse_lazy('booking_success')

    def test_func(self):
        return self.request.user == self.get_object().user

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        booking.delete()
        messages.success(request, "Booking deleted successfully.")
        return HttpResponseRedirect(self.success_url)
    





