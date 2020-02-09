from rest_framework import serializers
from .models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'chat', 'datetime', 'message']
        read_only_fields = ['author', 'datetime', 'chat']


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, required=False)

    class Meta:
        model = Chat
        fields = ['id', 'members', 'messages']
