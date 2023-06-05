from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('user/<slug:pk>/', ProfileView.as_view(), name='profile'),
]

