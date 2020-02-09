from rest_framework import serializers
from Users.serializers import UserSerializer
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'datetime']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'text', 'image', 'datetime', 'likes', 'comments'
        ]
