# Generated by Django 3.2.19 on 2023-06-08 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('date', 'time')},
        ),
    ]
