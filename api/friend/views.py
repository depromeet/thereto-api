from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.friend.models import Friend

from .serializers import (
    FriendSerializers,
)


class FriendListAPIView(ListAPIView):
    """
    친구 리스트 API
    """
    queryset = Friend.objects.all()
    serializer_class = FriendSerializers


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