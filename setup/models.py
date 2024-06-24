from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Level(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): 
        return str(self.user)

class Term(models.Model):
    title = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10, null=True, blank=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): 
        return str(self.user)

class Grade(models.Model):
    title = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10, null=True, blank=True)
    level_id = models.ForeignKey(Level, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True) 

    def __str__(self): 
        return str(self.user)

class Subject(models.Model):
    title = models.CharField(max_length=150)
    symbol = models.CharField(max_length=10, null=True, blank=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): 
        return str(self.user)

class House(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self): 
        return str(self.user)