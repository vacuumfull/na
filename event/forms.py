import datetime
from django import forms
from django.forms import ModelForm

from band.models import Band
from place.models import Place
from event.models import Event
from django.contrib.auth.models import User

class EventForm(forms.Form):
	"""Create Event Form"""
	title = forms.CharField(label='Название')
	description = forms.CharField(label='Краткое описание')
	image = forms.ImageField(label='Изображение')
	date = forms.DateField(initial=datetime.date.today, label='Дата проведения')
	price = forms.DecimalField(label='Стоиомсть')
	tags = forms.CharField(label='Тэги')	
	# когда будут роли надо исправить на музыкантов 
	musicians = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=False, is_staff=False, is_active=True), label='Музыканты')
	bands = forms.ModelChoiceField(queryset=Band.objects.published(), label='Коллективы')
	locations = forms.ModelChoiceField(queryset=Place.objects.all(), label='Заведения')


class EventUpdateForm(ModelForm):

	title = forms.CharField(label='Название')
	description = forms.CharField(label='Краткое описание')
	image = forms.ImageField(label='Изображение')
	date = forms.DateField(label='Дата проведения')
	price = forms.DecimalField(label='Стоиомсть')
	tags = forms.CharField(label='Тэги')	
	# когда будут роли надо исправить на музыкантов 

	class Meta:
		model = Event
		fields = ('title', 'image', 'description', 'date', 'price', 'tags',
				  'bands', 'musicians', 'locations')