from django.db import models
from django.conf import settings


class Friend(models.Model):
    """
    친구 모델
    """
    friend_1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='friend_1',
        on_delete=models.CASCADE,
        verbose_name='친구 요청을 보낸 사람'
    )
    friend_2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='friend_2',
        on_delete=models.CASCADE,
        verbose_name='친구 요청을 받는 사람'
    )

    is_active = models.BooleanField(
        '활성화 여부',
        default=False
    )
    is_confirm = models.BooleanField(
        '요청 수락 여부',
        default=False
    )

    confirm_at = models.DateTimeField(
        '수락일',
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        '생성일',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        '수정일',
        auto_now=True
    )

    class Meta:
        db_table = 'friends'
        verbose_name = '친구'
        verbose_name_plural = '친구들'

    def __str__(self):
        return "{} - {}".format(
            self.friend_1.name,
            self.friend_2.name
        )
