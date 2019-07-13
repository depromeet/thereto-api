from django.db import models
from django.conf import settings


def letter_image_path(instance, fielname):
    return 'letter/{}/{}'.format(
        instance.sender.id,
        filename
    )


class Letter(models.Model):
    """
    엽서 모델
    """
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='letter_sender',
        on_delete=models.CASCADE,
        verbose_name='보낸 사람'
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='letter_receiver',
        on_delete=models.CASCADE,
        verbose_name='받는 사람'
    )
    content = models.TextField(
        '내용',
        null=True,
        blank=True
    )
    image = models.ImageField(
        '이미지',
        null=True,
        blank=True,
        upload_to=letter_image_path
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
        db_table = 'letters'
        verbose_name = '엽서'
        verbose_name_plural = '엽서들'

    def __str__(self):
        return '{} - {}'.format(
            self.sender.name,
            self.receiver.name
        )
