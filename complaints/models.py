from django.db import models

# Create your models here.
class Complaint(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    massage = models.CharField(max_length=50)
    type = models.CharField(
        choices=[
            ('M','Maintainace'),
            ('S','Security'),
        ], max_length=1)
    is_solved = models.BooleanField(default=False)
    is_closed =models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

class Response(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    Complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    massage = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
