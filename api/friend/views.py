from django.db.models import Q

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.friend.models import Friend
from apps.user.models import User

from .serializers import (
    FriendSerializer, FriendSearchSerializer,
)


class FriendListAPIView(ListAPIView):
    """
    친구 리스트 API
    """
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            friend_1=self.request.user,
            is_active=True,
            is_confirm=True
        )

        return queryset


class FriendRequestAPIView(APIView):
    """
    친구 요청 API
    """
    def post(self, request, *args, **kwargs):
        receiver_id = kwargs.get('id')
        user = request.user

        if Friend.objects.filter(
            user=user,
            friend_2__id=receiver_id
        ).exists():
            return Response({
                'message': '이미 친구 신청을 한 사람입니다.'
            }, status=status.HTTP_400_BAD_REQUEST)

        Friend.objects.create(
            friend_1=user,
            friend_2__id=receiver_id
        )

        return Response({
            'message': '정상적으로 친구 요청을 하였습니다.'
        })


class FriendSearchAPIView(ListAPIView):
    """
    친구 검색 API
    """
    queryset = User.objects.all()
    serializer_class = FriendSearchSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.exclude(
            friend__friend_1__id=self.request.user.id
        )

        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(
                Q(name__icontains=name) |
                Q(nickname__icontainns=name)
            )

        return queryset
