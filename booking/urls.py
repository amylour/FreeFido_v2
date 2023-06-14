from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingsPage.as_view(), name='booking_home_page'),
    path('create/', views.CreateBooking.as_view(), name='booking_create'),
    path('booking/edit/<int:pk>/', views.BookingEdit.as_view(), name='booking_edit'),
    path('booking/delete/<int:pk>/',
         views.DeleteBooking.as_view(), name='booking_delete'),
]
