"""Message app"""
import os
from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models import Avg
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from uuslug import uuslug


class MessageManager(models.Manager):

    def unread(self, to_user):
        """All unread messages"""
        rows = Message.objects.filter(read=False, deleted=False, to_user=to_user).values('content', 'from_user', 'created_at')
        rows.order_by('created_at')
        result = list(rows)
    
        return result

    def user_history(self, from_user: User, to_user: User, offset: int=0):
        """All published post."""
        result = Message.objects.filter(read=True, deleted=False,
                                        from_user=from_user, to_user=to_user)[offset:offset+20]
        result.order_by('created_at')
        return result 


class Message(models.Model):
    """Message model."""

    content = RichTextField(blank=True, null=True,
                            verbose_name='Содержание')
    from_user = models.ForeignKey(User, verbose_name='Отправитель',
                             related_name='from_user')
    to_user = models.ForeignKey(User, verbose_name='Получатель',
                             related_name='to_user')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')
    read = models.BooleanField(default=False, verbose_name='Прочитано')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    def __str__(self):
        return "{}: {}".format(self.user, self.content)

    class Meta:
        ordering = ['created_at', 'from_user']
        verbose_name = 'Сообщения'
        verbose_name_plural = 'Сообщения'