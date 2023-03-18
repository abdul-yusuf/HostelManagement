from django.db import models

# Create your models here.

class Hostel(models.Model):
    name = models.CharField(max_length=50)

class Room(models.Model):
    room_no = models.CharField(max_length=15)
    block = models.CharField(max_length=10)
    members = models.ManyToManyField('authentication.User', related_name='room_members')
    hostel = models.ForeignKey('Hostel', on_delete=models.Case)


    