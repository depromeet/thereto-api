from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """
    유저 매니저
    """
    def create_superuser(self, username, name, password=None):
        if username is None:
            raise ValueError("아이디는 필수입니다.")

        user = self.model(
            username=username,
            name=name,
            is_admin=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(models.Model):
    """
    유저 모델
    """
    username = models.CharField(
        '아이디',
        max_length=50,
        help_text='관리자 로그인 전용으로만 사용할 예정'
    )
    name = models.CharField(
        '이름',
        max_length=50
    )
    nickname = models.CharField(
        '닉네임',
        max_length=50,
        null=True,
        blank=True
    )
    uid = models.CharField(
        '카카오 고유 ID',
        max_length=50,
        null=True,
        blank=True
    )
    date_joined = models.DateTimeField(
        '가입일',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        '활성화 여부',
        default=True
    )
    is_admin = models.BooleanField(
        '관리자 여부',
        default=False
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'name',
    ]

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __str__(self):
        return self.username
