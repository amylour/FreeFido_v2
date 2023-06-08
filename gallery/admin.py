from django.contrib import admin
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo_by', 'posted_on']
    list_filter = ['posted_on']
    search_fields = ['title', 'photo_by__username']
    date_hierarchy = 'posted_on'



