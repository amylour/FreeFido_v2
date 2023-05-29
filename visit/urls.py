from django.urls import path
from .views import VisitUs

urlpatterns = [
    path('', VisitUs.as_view(), name='visit_us'),
]
