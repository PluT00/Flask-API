from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Flask.permissions import IsAuthorOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class CommentAPIView(APIView):

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chat=chat, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

