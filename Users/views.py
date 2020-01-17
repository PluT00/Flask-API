from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MyUser
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
