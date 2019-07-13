from rest_framework import serializers

from apps.friend.models import Friend


class FriendSerializers(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Friend
        fields = [
            'name',
            'nickname',
            'image',
            'is_activ',
            'is_confirm',
            'confirm_at',
            'created',
        ]

    def get_name(self, obj):
        return obj.friend_2.name

    def get_nickname(self, obj):
        return obj.friend_2.nickname

    def get_image(self, obj):
        return obj.friend_2.get_image_url
