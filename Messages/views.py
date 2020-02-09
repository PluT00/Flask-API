from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from Flask.permissions import IsMember, IsAuthorOrReadOnly


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer

    def get_queryset(self):
        current_user = self.request.user
        return Chat.objects.filter(members__exact=current_user)


class MessageAPIView(ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_chats = Chat.objects.filter(members__exact=self.request.user)
        chat = user_chats.get(pk=self.kwargs['pk'])
        messages = Message.objects.filter(chat=chat)
        return messages

    def post(self, request, pk):
        user_chats = Chat.objects.filter(members__exact=self.request.user)
        chat = user_chats.get(pk=pk)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chat=chat, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
