"""Models for Events app"""
import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from uuslug import uuslug


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('event_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Event(models.Model):
    """Events model."""

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    image = models.ImageField(upload_to=image_path, verbose_name='Изображение')
    date = models.DateTimeField(blank=True, null=True,
                                verbose_name='Дата и время начала')
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                blank=True, null=True, verbose_name='Цена')

    owner = models.ForeignKey(User, verbose_name='Организатор')
    # bands = models.ManyToManyField(verbose_name='Команды')
    # musicians = models.ManyToManyField(verbose_name='Музыканты')
    # locations = models.ManyToManyField(verbose_name='Место проведения')

    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')
    # tags = models.ManyToManyField(verbose_name='Тэги')
    # ratings = models.ManyToManyField(verbose_name='Рейтинг')

    published = models.BooleanField(default=True, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.date)

    class Meta:
        ordering = ['date', 'title']
        verbose_name = 'События'
        verbose_name_plural = 'События'


@receiver(pre_save, sender=Event)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object."""
    instance.slug = uuslug(instance.title, instance=instance)