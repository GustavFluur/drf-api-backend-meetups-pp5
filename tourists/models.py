from django.db import models
from django.contrib.auth.models import User


class ExplorerProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    interest = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile & contact info:"


class Location(models.Model):
    place = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.place


class MeetUp(models.Model):
    activity = models.CharField(max_length=200)
    activity_created = models.DateField(auto_now_add=True)
    activity_place = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.activity