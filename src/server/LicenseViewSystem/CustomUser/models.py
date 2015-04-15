from django.db import models

# Create your models here.

class CustomUser(models.Model):
     username = models.CharField(max_length=30, unique=True)
     password = models.CharField(max_length=128)
     #last_login = models.DateTimeField(_('last login'), default=timezone.now)
     first_name = models.CharField(max_length=30, blank=True)
     last_name = models.CharField(max_length=30, blank=True)
     email = models.EmailField(blank=True)

     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['email']

     def get_fullname(self):
         full_name = "%s %s" % (self.first_name, self.last_name)
         return full_name.strip()

     class Meta:
         def __str__(self):
             return self.username