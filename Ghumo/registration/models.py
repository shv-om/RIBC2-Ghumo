from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_traveller = models.BooleanField(default=False)
    phone = models.CharField(max_length=10)

class Seller(models.Model):
    seller = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shopname = models.CharField(max_length=25)
    nearby_area = models.CharField(max_length=50)

    def __str__(self):
        return self.seller.username

class Artist(models.Model):
    artist = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)

    def __str__(self):
        return self.artist.username


class Traveller(models.Model):
    traveller = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.traveller.username