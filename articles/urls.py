from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='articles'),
    path('<slug:slug>/', views.ArticlePage.as_view(), name='article_page'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like')
]
