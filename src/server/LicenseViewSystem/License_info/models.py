from django.db import models

# Create your models here.
class License(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, primary_key=True)
    type = models.CharField(max_length=30)
    period = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name
