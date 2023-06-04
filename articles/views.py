from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.db.models import Q
from .models import Article
from .forms import ArticleForm, CommentForm

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


class AddArticle(LoginRequiredMixin, CreateView):
    """
    A model to create an article 
    """
    template_name = 'articles/article_create.html'
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddArticle, self).form_valid(form)


class ArticleList(generic.ListView):
    """
    A model to view the article cards, no more than 6 to a page
    """
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles/articles.html'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            articles = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(excerpt__icontains=query) |
                Q(content__icontains=query),
                status=1,
                is_deleted=False
            )
        else:
            articles = self.model.objects.filter(status=1, is_deleted=False)
        return articles


class ArticlePage(View):
    """
    A model to view an individual article & post a comment
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1, is_deleted=False)
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
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(
            approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

            # alert message to user if their comment has been approved & posted
            if comment.approved:
                messages.success(
                    request, 'Your comment has been approved and posted!')

            comments = article.comments.filter(
                approved=True).order_by('created_on')

        return render(
            request,
            'articles/article_page.html',
            {
                'article': article,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class ArticleLike(View):
    """
    A model to like/unlike the article
    """

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)

        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_page', args=[slug]))


class EditArticle(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit an article """
    template_name = 'articles/article_edit.html'
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

    def test_func(self):
        return self.request.user == self.get_object().author


class DeleteArticle(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete an article """
    model = Article
    success_url = '/articles/'

    def test_func(self):
        return self.request.user == self.get_object().author

    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        article.is_deleted = True
        article.save()
        messages.success(request, "Article deleted successfully.")
        return HttpResponseRedirect(self.success_url)
