from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'dog_name', 'breed', 'color',
                    'is_vaccinated', 'gender', 'date', 'time']
    list_filter = ['breed', 'is_vaccinated', 'gender']
    search_fields = ['user__username', 'dog_name']
    date_hierarchy = 'date'
