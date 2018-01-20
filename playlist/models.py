"""Models for Events app"""
import os
from uuid import uuid4

from ckeditor.fields import CKEditorWidget
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from uuslug import uuslug
from taggit.managers import TaggableManager


def image_path(_instance, filename):
    """Path and name to image file."""
    file_path = os.path.join('playlist_images', str(uuid4()))
    ext = filename.split('.')[-1]
    return '{}.{}'.format(file_path, ext)


class PlaylistManager(models.Manager):
	"""Playlist model manager"""

	def user_items(self, creator):
		"""User created blogs"""
		result = Playlist.objects.filter(creator=creator).values('id', 'name', 'annotation', 'content', 'image', 'published', 'slug', 'created_at').reverse()
		result_list = [i for i in result]
		return result_list

	def published(self):
		"""All published playlists."""
		result = Playlist.objects.filter(published=True).order_by('created_at').reverse()
		result.order_by('created_at', 'name')
		return result


class Playlist(models.Model):
	"""Playlist Model"""
	name = models.CharField(max_length=200, verbose_name='Название')
	annotation = models.TextField(verbose_name='Аннотация')
	content = models.TextField(verbose_name='Содержание')
	image = models.ImageField(upload_to=image_path, null=True, blank=True,
                              verbose_name='Титульное изображение')
	creator = models.ForeignKey(User, on_delete=models.CASCADE,
									verbose_name='Создатель',
									related_name='creator')
	tags = TaggableManager(verbose_name='Тэги', related_name='playlist_tags')
	published = models.BooleanField(default=False, verbose_name='Активно')
	slug = models.SlugField(max_length=200, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = PlaylistManager()
	

	def __str__(self):
		return self.name
    

	class Meta:
		ordering = ['created_at', 'name', 'creator']
		verbose_name = 'Плейлист'
		verbose_name_plural = 'Плейлисты'


@receiver(pre_save, sender=Playlist)
def created_slug(sender, instance, **_):
    """Generate custom slug before save object."""
    if instance.pk is None:
        instance.slug = uuslug(instance.name, instance=instance)