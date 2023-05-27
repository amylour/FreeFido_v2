from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles/articles.html'
    paginate_by = 6
