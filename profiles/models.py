from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField


class Profile(models.Model):
    """ profile model """
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[350, 350],
        quality=75,
        upload_to="profiles/",
        force_format="WEBP",
        blank=False,
    )
    display_name = models.CharField(max_length=30, blank=True, null=True)
    bio = RichTextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """ create or update the user profile """
    if created:
        Profile.objects.create(user=instance)