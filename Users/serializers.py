from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        read_only_fields = (
            'is_active', 'is_staff', 'last_login', 'is_superuser', 'date_joined',
            'user_permissions', 'groups'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
