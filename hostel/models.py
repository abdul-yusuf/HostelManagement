from django.db import models

# Create your models here.

class Hostel(models.Model):
    name = models.CharField(max_length=50)

class Room(models.Model):
    room_no = models.CharField(max_length=15)
    hostel = models.ForeignKey('Hostel', on_delete=models.Case)
    