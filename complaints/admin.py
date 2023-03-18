from django.contrib import admin
from .models import Complaint, Response

# Register your models here.

admin.site.register(Complaint)
admin.site.register(Response)