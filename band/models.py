# -*- coding: utf-8 -*-
"""Models for Bands app."""
import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from uuslug import uuslug


def image_path(_instance, filename):
    """Path and name to logo file."""
    file_path = os.path.join('band_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class BandManager(models.Manager):

    def user_items(self, owner):
        """User created blogs"""
        result = Band.objects.filter(owner=owner).values(
            'id', 'name', 'description', 'image', 'published', 'slug', 'created_at')
        result_list = [i for i in result]
        return result_list


    def published(self):
        """All published post."""
        result = Band.objects.filter(published=True).order_by('created_at').reverse()
        return result


class Band(models.Model):
    """Bands model."""

    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    image = models.ImageField(upload_to=image_path, verbose_name='Логотип')

    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE,
                              verbose_name='Организатор')
    members = models.ManyToManyField(User, related_name='members',
                                     verbose_name='Участники')

    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')
    tags = TaggableManager(verbose_name='Тэги', related_name='band_tags')

    published = models.BooleanField(default=True, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BandManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'created_at']
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллективы'


class CommentManager(models.Manager):
    """Events comments manager."""

    def get_last_comments(self, band_id: int, offset: int=0):
        """Get last comment with offset in event."""
        rows = Comment.objects.filter(
            band=band_id, published=True).order_by('created_at').reverse()[offset:offset+20]
        return rows


class Comment(models.Model):
    """Events comment model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='band_commentator')
    band = models.ForeignKey(Band, on_delete=models.CASCADE,
                              verbose_name='Запись')
    content = models.CharField(max_length=250, verbose_name='Содержание')
    published = models.BooleanField(default=True, verbose_name='Активно')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()

    def __str__(self):
        return "{}: {}".format(self.user, self.content)

    class Meta:
        ordering = ['created_at', 'user']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


@receiver(pre_save, sender=Band)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object"""
    if instance.pk is None:
        instance.slug = uuslug(instance.name, instance=instance)
