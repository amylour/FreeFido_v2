from . import views
from django.urls import path

urlpatterns = [
    path('', views.Gallery.as_view(), name='gallery'),
    path('add_photo/', views.AddPhoto.as_view(), name='add_photo'),
    path('delete_photo/<int:pk>/', views.DeletePhoto.as_view(), name='delete_photo'),
]
