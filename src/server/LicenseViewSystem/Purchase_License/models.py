from django.db import models
from django.contrib.auth.admin import User
from License_info.models import License

# Create your models here.

class Purchase(models.Model):
    user = models.ForeignKey("User")
    license_info = models.ForeignKey("License_info")


    date = models.DateTimeField('date published')
