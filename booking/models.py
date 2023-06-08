from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

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


TIME_CHOICES = [
    ('08:00 - 09:00', '08:00 - 09:00'),
    ('09:00 - 10:00', '09:00 - 10:00'),
    ('10:00 - 11:00', '10:00 - 11:00'),
    ('11:00 - 12:00', '11:00 - 12:00'),
    ('12:00 - 13:00', '12:00 - 13:00'),
    ('13:00 - 14:00', '13:00 - 14:00'),
    ('14:00 - 15:00', '14:00 - 15:00'),
    ('15:00 - 16:00', '15:00 - 16:00'),
    ('16:00 - 17:00', '16:00 - 17:00'),
    ('17:00 - 18:00', '17:00 - 18:00'),
    ('18:00 - 19:00', '18:00 - 19:00'),
    ('19:00 - 20:00', '19:00 - 20:00'),
    ]


class Booking(models.Model):
    """ A model for making a booking """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    class Meta:
        """ Order bookings by date """
        ordering = ["-date"]
        unique_together = ['date', 'time']



    def __str__(self):
        return f"Booking for {self.user.username}"
