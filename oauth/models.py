from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class GoogleManager(models.Manager):
	pass

class Google(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,
							 verbose_name='Пользователь')
	system_id = models.CharField(max_length=250, verbose_name='Системное имя пользователя')
	access_token = models.TextField(blank=True, verbose_name='Токен пользователя')
	
	objects = GoogleManager()


class VkontakteManager(models.Manager):
	pass

class Vkontakte(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,
							 verbose_name='Пользователь')
	system_id = models.CharField(max_length=250, verbose_name='VK Id пользователя')
	access_token = models.TextField(blank=True, verbose_name='Токен пользователя')
	
	objects = GoogleManager()