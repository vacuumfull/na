"""Models for places app."""
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
    file_path = os.path.join('place_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


def icon_path(_instance, filename):
    """Path and name to ico file."""
    file_path = os.path.join('place_icons', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Place(models.Model):
    """Places model."""
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    image = models.ImageField(upload_to=image_path, verbose_name='Логотип')
    icon = models.ImageField(upload_to=icon_path, verbose_name='Иконка')

    owner = models.ForeignKey(
        User, related_name='manager',
        blank=True, null=True,
        verbose_name='Владелец')
    musicians = models.ManyToManyField(
        User, related_name='musicians',
        blank=True,
        verbose_name='Музыканты заведения')
    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')
    # tags = models.ManyToManyField(verbose_name='Тэги')
    # ratings = models.ManyToManyField(verbose_name='Рейтинг')

    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'created_at']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Location(models.Model):
    """Locatino model for Place."""

    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              verbose_name='Заведение')
    maps = models.CharField(max_length=100, verbose_name='Координаты на карте')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    worktime = models.TextField(verbose_name='Информация о работе')

    def __str__(self):
        return self.address

    class Meta:
        ordering = ['address']
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


@receiver(pre_save, sender=Place)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object"""
    instance.slug = uuslug(instance.title, instance=instance)
