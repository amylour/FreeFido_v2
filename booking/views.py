from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views import generic, View
from django.views.generic import CreateView, ListView, DetailView, DeleteView, TemplateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from .models import Booking
from .forms import BookingForm

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


class BookingsPage(TemplateView):
    template_name = 'booking/bookings_home_page.html'


class CreateBooking(LoginRequiredMixin, CreateView):
    """
    A view to create a booking
    """
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_create.html'
    success_url = reverse_lazy('booking_success')

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        # check the number of active bookings for the user
        user = self.request.user
        active_bookings_count = Booking.objects.filter(user=user).count()

        if active_bookings_count >= 4:
            # show an error message and redirect to booking if 4 bookings active
            messages.error(
                self.request, 'You have reached the maximum number of bookings.')
            return HttpResponseRedirect(self.success_url)
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
        # show active bookings by user by date
        return Booking.objects.filter(user=self.request.user).order_by('-date')


class BookingEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit an article """
    template_name = 'booking/booking_edit.html'
    model = Booking
    form_class = BookingForm

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        # Return the URL of the booking success page
        return reverse('booking_success')

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
    
