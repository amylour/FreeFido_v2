# Generated by Django 3.2.19 on 2023-06-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_galleryimage_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image_description',
            field=models.CharField(max_length=100),
        ),
    ]
