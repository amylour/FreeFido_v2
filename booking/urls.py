from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.CreateBooking.as_view(), name='booking_create'),
    path('success/',views.ActiveBookings.as_view(), name='booking_success'),
]
