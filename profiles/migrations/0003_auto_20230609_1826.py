# Generated by Django 3.2.19 on 2023-06-09 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_profile_biop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='biop',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
