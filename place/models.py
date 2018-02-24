# -*- coding: utf-8 -*-
"""Models for places app."""
import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Avg
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
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


class PlaceManager(models.Manager):
    """Place manager."""

    def user_items(self, owner):
        result = Place.objects.filter(owner=owner).values('id', 'title', 'description', 'icon', 'published', 'slug', 'created_at')
        result_list = [i for i in result]
        return result_list

    def published(self):
        result = Place.objects.filter(published=True).order_by('created_at').reverse()
        return result

    def last_published(self):
        """Last published place."""
        result = Place.objects.published()[:16]
        return result


class Place(models.Model):
    """Places model."""

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    image = models.ImageField(upload_to=image_path, verbose_name='Логотип')
    icon = models.ImageField(upload_to=icon_path, blank=True, verbose_name='Иконка')

    owner = models.ForeignKey(
        User, related_name='place_owner',
        blank=True, null=True, on_delete=models.SET_NULL,
        verbose_name='Владелец')
    musicians = models.ManyToManyField(
        User, related_name='place_musicians',
        blank=True,
        verbose_name='Музыканты заведения')
    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')

    tags = TaggableManager(verbose_name='Тэги', related_name='place_tags')
    # ratings = models.ManyToManyField(verbose_name='Рейтинг')
    coordinates = models.CharField(max_length=150, verbose_name='Координаты', default='')
    worktime = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Время работы')
    address = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name='Адрес')

    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PlaceManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'created_at']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class CommentManager(models.Manager):
    """Place comments manager."""
    
    def get_last_comments(self, place_id: str, offset: int=0):
        """Get last comment with offset in place."""
        rows = Comment.objects.filter(
            place=place_id, published=True).order_by('created_at').reverse()[offset:offset+20]
        return rows


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='place_commentator')
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
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


class RatingManager(models.Manager):
    """Place rating manager."""
    
    def rating(self, place_id):
        rows = Rating.objects.filter(place=place_id)
        rate = rows.aggregate(Avg('value')).get('value__avg', 0)
        rate = str(round(rate, 1))
    
        if rate[-1] == '0':
            shift = len(rate) - 2
            rate = rate[:shift]
            
        return rate


    def average(self, place_id: int, user: User) -> dict:
        """Average place rating.
        is_vote - check voted this user in current place
        value - average place rating
        """
        rows = Rating.objects.filter(place=place_id)
        result = {
            'is_vote': rows.filter(user=user).exists(),
            'value': rows.aggregate(Avg('value')).get('value__avg', 0),
            'total': rows.count(),
        }
        return result


    def average_unlogin(self, place_id: int) -> dict:

        rows = Rating.objects.filter(place=place_id)
        result = {
            'value': rows.aggregate(Avg('value')).get('value__avg', 0),
            'total': rows.count(),
        }
        return result


class Rating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              verbose_name='Запись')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='place_voted')
    value = models.IntegerField(verbose_name='Оценка')

    objects = RatingManager()

    class Meta:
        unique_together = ('place', 'user')


@receiver(pre_save, sender=Place)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object"""
    if instance.pk is None:
        instance.slug = uuslug(instance.title, instance=instance)
