# Generated by Django 3.2.19 on 2023-05-31 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_publish_article_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='approved',
        ),
    ]