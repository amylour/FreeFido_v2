from . import views
from django.urls import path


urlpatterns = [
    path('', views.ArticleList.as_view(), name='articles'),
    path('create/', views.AddArticle.as_view(), name='article_create'),
    path('<slug:slug>/', views.ArticlePage.as_view(), name='article_page'),
    path('like/<slug:slug>', views.ArticleLike.as_view(), name='article_like'),
    path('edit/<slug:slug>', views.EditArticle.as_view(), name='article_edit'),
    path('delete/<slug:slug>', views.DeleteArticle.as_view(), name='article_delete')
]
