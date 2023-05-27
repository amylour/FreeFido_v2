from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='articles')
]