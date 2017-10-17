"""Models for Events app"""
import os
from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from uuslug import uuslug

from event.models import Event
from place.models import Place


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('blog_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class BlogManager(models.Manager):
    """Blog manager."""

    def last_published(self):
        """Last published blog."""
        result = Blog.objects.filter(published=True)[:4]
        return result


class Blog(models.Model):
    """Blogs model."""

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    annotation = models.TextField(verbose_name='Аннотация')
    content = RichTextField(blank=True, null=True,
                            verbose_name='Содержание')
    image = models.ImageField(upload_to=image_path,
                              verbose_name='Титульное изображение')

    author = models.ForeignKey(User, verbose_name='Автор')
    event = models.ForeignKey(Event, blank=True, null=True,
                              verbose_name='Событие')
    place = models.ForeignKey(Place, blank=True, null=True,
                              verbose_name='Место')
    # tags = models.ManyToManyField(verbose_name='Тэги')
    # ratings = models.ManyToManyField(verbose_name='Рейтинг')

    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at', 'title', 'author']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


@receiver(pre_save, sender=Blog)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object."""
    instance.slug = uuslug(instance.title, instance=instance)
