from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=20, unique=True)
    location = models.TextField()

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.IntegerField()
    room_type = models.CharField(max_length=20)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

class Reservation(models.Model):
    reservation = models.IntegerField(auto_created=True, unique=True)
    reservation_start = models.DateField()
    reservation_end = models.DateField()
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reservation)