from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Article


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles/articles.html'
    paginate_by = 6


class ArticlePage(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(
            approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'articles/article_page.html',
            {
                'article': article,
                'comments': comments,
                'liked': liked
            },
        )
