# Generated by Django 3.2.19 on 2023-06-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_article_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
