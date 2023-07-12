from django.urls import path
from .views import ProfileView, ProfileEdit

urlpatterns = [
    path('user/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/<int:pk>/', ProfileEdit.as_view(), name='profile_edit'),
]
