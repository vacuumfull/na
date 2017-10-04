"""Models for Events app"""
import os
from uuid import uuid4

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from uuslug import uuslug


def img_path(_instance, filename):
    """Custom path and name to image file"""
    file_path = os.path.join('blog_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Blog(models.Model):
    """Blogs model"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    author = models.ForeignKey(User, verbose_name='Автор')
    image = models.ImageField(upload_to=img_path,
                              verbose_name='Титульное изображение')
    annotation = models.TextField(verbose_name='Аннотация')
    content = models.TextField(blank=True, null=True,
                               verbose_name='Содержание')
    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at', 'title', 'author']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


@receiver(pre_save, sender=Blog)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object"""
    instance.slug = uuslug(instance.title, instance=instance)
