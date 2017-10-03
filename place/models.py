"""Models for places app"""
import os
from random import randint
from uuid import uuid4

from django.db import models
from uuslug import slugify


def logo_path(_instance, filename):
    """Custom path and name to logo file"""
    file_path = os.path.join('place_logo', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class Place(models.Model):
    """Places model"""
    title = models.CharField(max_length=200, verbose_name='Название')
    address = models.CharField(max_length=240, verbose_name='Адрес')
    logo = models.ImageField(upload_to=logo_path, verbose_name='Логотип')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание')
    published = models.BooleanField(default=False, verbose_name='Активно')
    slug = models.SlugField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                '{}-{}'.format(randint(1000, 9999), self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'created_at']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
