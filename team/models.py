"""Models for team app"""
import os
from random import randint
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User
from uuslug import slugify


def logo_path(_instance, filename):
    """Custom path and name to logo file"""
    file_path = os.path.join('team_logo', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Team(models.Model):
    """ Teams model"""
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    logo = models.ImageField(upload_to=logo_path,
                             verbose_name='Логотип')
    member = models.ManyToManyField(User, verbose_name='Участники')
    published = models.BooleanField(default=False, verbose_name='Активны')
    slug = models.SlugField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                '{}-{}'.format(randint(1000, 9999), self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'created_at']
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллективы'
