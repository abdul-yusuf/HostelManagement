from django.db import models

# Create your models here.
class Complaint(models.Model):

    massage = models.CharField(max_length=50)
    is_solved = models.BooleanField(default=False)
    is_closed =models.BooleanField(default=False)

class Response(models.Model):
    massage = models.CharField(max_length=50)
    
    # class Meta:
    #     verbose_name = _("Complaint")
    #     verbose_name_plural = _("Complaints")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Complaint_detail", kwargs={"pk": self.pk})
