from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    """ A model for making a booking """
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    dog_name = models.CharField(max_length=20)
    breed = models.CharField(max_length=30, choices=BREED_CHOICES)
    color = models.CharField(max_length=30)
    is_vaccinated = models.BooleanField(default=False)
    gender = models.CharField(max_length=6, choices=[
                              ('M', 'Male'), ('F', 'Female')])
    date = models.DateField()
    time = models.TimeField()


    def __str__(self):
        return f"Booking for {self.user.username}"
