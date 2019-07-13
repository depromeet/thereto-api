from rest_framework.generics import ListAPIView

from apps.friend.models import Friend


class FriendListAPIView(ListAPIView):
    """
    친구 리스트 API
    """
    queryset = Friend.objects.all()
