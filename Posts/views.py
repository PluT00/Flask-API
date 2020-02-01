from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from Flask.permissions import IsAuthorOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

