from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingsPage.as_view(), name='bookings_home_page'),
    path('create/', views.CreateBooking.as_view(), name='booking_create'),
    path('success/',views.ActiveBookings.as_view(), name='booking_success'),
    path('booking/delete/<int:pk>/',
         views.DeleteBooking.as_view(), name='booking_delete'),
]
