"""Models for Events app"""
import os
from uuid import uuid4

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Avg
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from uuslug import uuslug
from taggit.managers import TaggableManager

from band.models import Band
from place.models import Place


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('event_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class EventManager(models.Manager):
    """Event manager."""

    def user_items(self, owner):
        result = Event.objects.filter(owner=owner).values('id', 'title', 'description', 'image', 'published', 'slug', 'date', 'created_at').reverse()
        result_list = [i for i in result]
        return result_list

    def last_published(self):
        """Last published upcoming events."""
        result = Event.objects.upcoming()[:4]
        return result

    def upcoming(self):
        """Upcoming events."""
        result = Event.objects.filter(
            published=True, date__gte=timezone.now())
        return result

    def published(self):
        """All published post."""
        result = Event.objects.filter(published=True)
        result.order_by('date')
        return result


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

    owner = models.ForeignKey(
        User, related_name='event_owner',
        on_delete=models.CASCADE,
        verbose_name='Организатор')
    bands = models.ManyToManyField(
        Band, related_name='event_bands',
        blank=True,
        verbose_name='Команды')
    musicians = models.ManyToManyField(
        User, related_name='event_musicians',
        blank=True,
        verbose_name='Музыканты')
    locations = models.ManyToManyField(
        Place, related_name='event_location',
        blank=True,
        verbose_name='Место проведения')

    tags = TaggableManager(verbose_name='Тэги', related_name='event_tags')
    socials = JSONField(blank=True, null=True,
                        verbose_name='Социальные ссылки')
    # ratings = models.ManyToManyField(verbose_name='Рейтинг')

    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EventManager()

    def __str__(self):
        return '{} ({})'.format(self.title, self.date)

    class Meta:
        ordering = ['date', 'title']
        verbose_name = 'События'
        verbose_name_plural = 'События'


class CommentManager(models.Manager):
    """Events comments manager."""

    def get_last_comments(self, event_id: int, offset: int=0):
        """Get last comment with offset in event."""
        rows = Comment.objects.filter(
            event=event_id, published=True).order_by('created_at').reverse()[offset:offset+20]
        return rows


class Comment(models.Model):
    """Events comment model."""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='event_commentator')
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
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
    """Events rating manager."""

    def rating(self, event_id):
        rows = Rating.objects.filter(event=event_id)
        rate = rows.aggregate(Avg('value')).get('value__avg', 0)
        rate = str(round(rate, 1))
    
        if rate[-1] == '0':
            shift = len(rate) - 2
            rate = rate[:shift]
        
        return rate


    def average(self, event_id: int, user: User) -> dict:
        """Average event rating.
        is_vote - check voted this user in current event
        value - average event rating
        """
        rows = Rating.objects.filter(event=event_id)
        result = {
            'is_vote': rows.filter(user=user).exists(),
            'value': rows.aggregate(Avg('value')).get('value__avg', 0),
            'total': rows.count(),
        }
        return result


    def average_unlogin(self, event_id: int) -> dict:

        rows = Rating.objects.filter(event=event_id)
        result = {
            'value': rows.aggregate(Avg('value')).get('value__avg', 0),
            'total': rows.count(),
        }
        return result


class Rating(models.Model):
    """Events Rating model."""

    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              verbose_name='Запись')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             related_name='event_voted')
    value = models.IntegerField(verbose_name='Оценка')

    objects = RatingManager()

    class Meta:
        unique_together = ('event', 'user')


@receiver(pre_save, sender=Event)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object."""
    if instance.pk is None:
        instance.slug = uuslug(instance.title, instance=instance)
