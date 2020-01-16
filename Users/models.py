from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.username
