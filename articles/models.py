from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from djrichtextfield.models import RichTextField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Article(models.Model):
    """ A model to create and manage articles """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="article_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, default='default alt', null=False, blank=False)
    excerpt = models.TextField(max_length=300, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(max_length=5000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='article_like',
                                   blank=True)
    is_deleted = models.BooleanField(default=False)                        

    class Meta:
        """ Order posts by created on date """
        ordering = ["-created_on"]

    # Django magic method that returns a string rep of an object
    def __str__(self):
        return self.title

    # Return number of likes
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """ A model to allow and manage comments on an article """
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name="comments", null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
