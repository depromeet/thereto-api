from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from apps.user.models import User
from .serializers import (
    LoginSerializer,
)

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginAPIView(GenericAPIView):
    serializers_class = LoginSerializer

    def generate_jwt_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return token

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.data
        uid = data.get('uid')
        
        user = User.objects.filter(uid=uid)

        if user.exists():
            user_token = self.generate_jwt_token(user)

            return Response({
                'token': user_token,
                'message': '로그인에 성공했습니다.'
            })

        new_user = User.objects.create(
            name=data.get('name')
        )

        new_user_token = self.generate_jwt_token(new_user)

        return Response({
            'token': new_user_token,
            'message': '새로운 유저가 생성되었습니다.'
        }, status=status.HTTP_201_CREATED)


class ChangeNickNameAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
