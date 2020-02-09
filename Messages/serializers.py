from rest_framework import serializers
from Users.serializers import UserSerializer
from .models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Message
        fields = ['id', 'author', 'chat', 'datetime', 'message']
        read_only_fields = ['author', 'datetime', 'chat']


class ChatSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['id', 'members']
