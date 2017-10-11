"""User extends model."""
import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


def avatar_path(_instance, filename):
    """Path and name to avatar."""
    file_path = os.path.join('avatars', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class UserExtend(models.Model):
    """User extend model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=avatar_path, verbose_name='Аватар')

    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')


class UserSettings(models.Model):
    """User settings model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alert_comment = models.BooleanField(
        default=False, verbose_name='Уведомлять об ответах на комментарии')
    alert_blog = models.BooleanField(
        default=False, verbose_name='Уведомлять о новых коментарии к постам')
    alert_rating = models.BooleanField(
        default=False, verbose_name='Уведомлять об оценках записей')
    alert_link = models.BooleanField(
        default=False,
        verbose_name='Уведомлять при прикреплении к месту или событию')
    deleted = models.BooleanField(
        default=False, verbose_name='Пользователь удален')
