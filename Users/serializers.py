from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = MyUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            country = validated_data['country'],
            city = validated_data['city'],
            bio = validated_data['bio'],
            avatar = validated_data['avatar']
        )
        user.set_password(validated_data['password'])
        user.friends.set(validated_data['friends'])
        user.save()
        return user

    class Meta:
        model = MyUser
        fields = [
            'id', 'date_joined', 'last_login', 'is_superuser', 'is_staff',
            'is_active', 'username', 'password', 'email', 'first_name',
            'last_name', 'country', 'city', 'bio', 'avatar', 'friends'
        ]
        read_only_fields = (
            'is_active', 'is_staff', 'last_login', 'is_superuser', 'date_joined'
        )
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'country': {'required': False},
            'city': {'required': False},
            'bio': {'required': False},
            'avatar': {'required': False},
            'friends': {'required': False},
        }
