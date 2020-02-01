from django.db import models
from Users.models import MyUser


class Post(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(blank=True, default=0)

    def __str__(self):
        text = ' '.join(self.text.split(' ')[:4])
        author = self.author.username
        return author + ':' + text


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=3000)
    datetime = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True)

