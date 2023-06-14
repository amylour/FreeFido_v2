from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Booking
from .forms import BookingForm


class BookingsPage(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_home_page.html'
    context_object_name = 'booking'


class CreateBooking(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_create.html'
    success_url = reverse_lazy('booking_home_page')

    def form_valid(self, form):
        # Set the current user as the booking user
        form.instance.user = self.request.user

        # Check the number of active bookings for the current user
        active_bookings_count = Booking.objects.filter(
            user=self.request.user).count()

        # Limit the maximum number of active bookings to 4
        if active_bookings_count >= 4:
            messages.error(
                self.request, "You have reached the maximum number of active bookings.")
            return redirect(self.success_url)

        return super().form_valid(form)


class BookingEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_edit.html'
    success_url = reverse_lazy('booking_home_page')

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Exclude date and time fields from cleaned data
        cleaned_data = form.cleaned_data
        new_date = cleaned_data.get('date')
        new_time = cleaned_data.get('time')

        # Check if the new time and date are available
        if new_date and new_time:
            existing_booking = Booking.objects.filter(
                date=new_date, time=new_time).exclude(pk=self.object.pk).first()
            if existing_booking:
                messages.error(
                    self.request, 'This time and date is already booked.')

        return super().form_valid(form)





class DeleteBooking(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'booking/booking_confirm_delete.html'
    success_url = '/booking_home_page/'

    def test_func(self):
        booking = self.get_object()
        return self.request.user == booking.user



