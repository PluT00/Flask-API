from django.db import models
from Users.models import MyUser


class Chat(models.Model):
    members = models.ManyToManyField(MyUser)

    def __str__(self):
        return ", ".join(p.username for p in self.members.all())


class Message(models.Model):
    message = models.TextField(max_length=10000)
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages", blank=True, null=True
    )
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, blank=True)
    datetime = models.DateTimeField(auto_now=True)

