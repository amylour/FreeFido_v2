from django.urls import path
from .views import ProfileView, ProfileEdit

urlpatterns = [
    path('user/<slug:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/<slug:pk>/', ProfileEdit.as_view(), name='profile_edit')
]

