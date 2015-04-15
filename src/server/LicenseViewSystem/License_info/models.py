from django.db import models
from django.conf import settings


# Create your models here.


class License(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, primary_key=True)
    type = models.CharField(max_length=30, primary_key=True)
    period = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_period(self):
        return self.period


class Buy(models.Model):
    username = models.ManyToManyField(settings.AUTH_USER_MODEL)
    license = models.ForeignKey(License)

