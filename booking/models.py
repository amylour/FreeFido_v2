from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from agenda.models import Task

# Breed choices for user in profile dropdown menu in tuple format for database value and site viewable value for the user
BREED_CHOICES = [
    ('Australian Shepard', 'Australian Shepard'),
    ('Bassett Hound', 'Bassett Hound'),
    ('Beagle', 'Beagle'),
    ('Belgian Shepard', 'Belgian Shepard'),
    ('Bernese', 'Bernese'),
    ('Bichon Frise', 'Bichon Frise'),
    ('Boston Terrier', 'Boston Terrier'),
    ('Boxer', 'Boxer'),
    ('Bulldog', 'Bulldog'),
    ('Chihuahua', 'Chihuahua'),
    ('Collie', 'Collie'),
    ('Corgi', 'Corgi'),
    ('Dachshund', 'Dachshund'),
    ('Doberman', 'Doberman'),
    ('English Mastiff', 'English Mastiff'),
    ('Fox Hound', 'Foxhound'),
    ('Greyhound', 'Greyhound'),
    ('German Shepherd', 'German Shepherd'),
    ('Golden Retriever', 'Golden Retriever'),
    ('Great Dane', 'Great Dane'),
    ('Husky', 'Husky'),
    ('Labrador Retriever', 'Labrador Retriever'),
    ('Lurcher', 'Lurcher'),
    ('Poodle', 'Poodle'),
    ('Rottweiler', 'Rottweiler'),
    ('Saint Bernard', 'Saint Bernard'),
    ('Shih Tzu', 'Shih Tzu'),
    ('Spaniel', 'Spaniel'),
    ('Terrier', 'Terrier'),
    ('Weimaraner', 'Weimaraner'),
    ('Other', 'Other'),
]


# generate hourly time slots from 8 am to 8 pm
TIME_CHOICES = []
start_time = datetime.strptime("08:00", "%H:%M")
end_time = datetime.strptime("20:00", "%H:%M")

while start_time < end_time:
    time_slot = start_time.strftime(
        "%H:%M") + " - " + (start_time + timedelta(hours=1)).strftime("%H:%M")
    TIME_CHOICES.append((time_slot, time_slot))
    start_time += timedelta(hours=1)


class Booking(models.Model):
    """ A model for making a booking """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    dog_name = models.CharField(max_length=20)
    breed = models.CharField(max_length=30, choices=BREED_CHOICES)
    color = models.CharField(max_length=30)
    is_vaccinated = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=[
                              ('M', 'Male'), ('F', 'Female')])
    date = models.DateField(default=datetime.now, blank=True)
    time = models.CharField(max_length=20, choices=TIME_CHOICES, default="11:00 - 12:00")

    dog_name2 = models.CharField(max_length=20, blank=True, null=True)
    breed2 = models.CharField(
        max_length=30, choices=BREED_CHOICES, blank=True, null=True)
    color2 = models.CharField(max_length=30, blank=True, null=True)
    is_vaccinated2 = models.BooleanField(default=False, blank=True, null=True)
    gender2 = models.CharField(max_length=6, choices=[
                              ('M', 'Male'), ('F', 'Female')], blank=True, null=True)

    class Meta:
        """ Order bookings by date """
        ordering = ["-date"]
        unique_together = ['date', 'time']

    def __str__(self):
        return f"Booking for {self.user.username}"
