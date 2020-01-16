from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000)
    friends = models.ManyToManyField("self", blank=True)
