from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField()

    def __str__(self):
        return self.username

class Hotel(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.IntegerField()
    room_type = models.CharField(max_length=20)
    description = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return str(self.number)

class Reservation(models.Model):
    reservation_start = models.DateField()
    reservation_end = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation_user')

class Image_room(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/images/')
    description = models.CharField(max_length=50, blank=True)