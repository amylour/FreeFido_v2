# Generated by Django 3.2.19 on 2023-06-08 19:33

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('photo', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='photo')),
                ('image_alt', models.CharField(default='default alt', max_length=100)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('photo_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_on'],
            },
        ),
    ]
