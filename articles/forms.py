from .models import Article, Comment
from django import forms
from djrichtextfield.widgets import RichTextWidget


class ArticleForm(forms.ModelForm):
    """ Form to create an article """
    class Meta:
        model = Article
        fields = ['title', 'featured_image', 'image_alt', 'excerpt','content']

        contents = forms.CharField(widget=RichTextWidget())

        widget = {
            "excerpt": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Article Title",
            "featured_image": "Article Image",
            "image_alt": "Describe Image",
            "excerpt": "Excerpt",
            "content": "Content",
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
