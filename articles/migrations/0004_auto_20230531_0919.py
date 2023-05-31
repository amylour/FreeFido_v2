# Generated by Django 3.2.19 on 2023-05-31 09:19

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_post_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_alt',
            field=models.CharField(default='default alt', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=djrichtextfield.models.RichTextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='article',
            name='excerpt',
            field=models.TextField(max_length=300),
        ),
    ]