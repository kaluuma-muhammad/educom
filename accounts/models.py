from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True, null=True)
    address = models.CharField(max_length=12, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    image = models.ImageField(default='default.png', blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self): 
        return str(self.user)