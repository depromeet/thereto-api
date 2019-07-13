from rest_framework import serializers

from apps.user.models import User


class LoginSerializer(serializers.Serializer):
    uid = serializers.CharField()
    name = serializers.CharField()
    image = serializers.ImageField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'nickname',
        ]