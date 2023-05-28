from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin

# decorator to register article model and article admin class with admin site


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'article', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
