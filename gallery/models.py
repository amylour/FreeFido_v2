from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class GalleryImage(models.Model):
    """ A model to upload an image to the gallery wall """
    photo_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gallery_posts")
    title = models.CharField(max_length=100, unique=True)
    photo = CloudinaryField(
        'photo', default='placeholder', null=False, blank=False)
    image_description = models.CharField(
        max_length=100, default='', null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Order images by created on date """
        ordering = ["-posted_on"]

    def __str__(self):
        return self.photo_by.username
