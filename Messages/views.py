from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from Flask.permissions import IsMember, IsAuthorOrReadOnly


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer
    permission_classes = [IsMember]

    def get_queryset(self):
        current_user = self.request.user
        return Chat.objects.filter(members__exact=current_user)


class MessageAPIView(APIView):

    def post(self, request, pk):
        chat = Chat.objects.get(pk=pk)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chat=chat, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

