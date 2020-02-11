from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView, CreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny
from .models import MyUser
from .serializers import UserSerializer


class UserListAPIView(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
