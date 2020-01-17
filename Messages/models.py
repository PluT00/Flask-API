from django.db import models
from Users.models import MyUser


class Chat(models.Model):
    members = models.ManyToManyField(MyUser)

    def __str__(self):
        return ", ".join(p.username for p in self.members.all())
