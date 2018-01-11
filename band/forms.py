from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User

from band.models import Band

queryset = User.objects.values('id', 'username')
members = [(q['id'], q['username']) for q in queryset]


class BandForm(forms.Form):
	"""Band Form"""
	name = forms.CharField(label='Название')
	description = forms.CharField(label='Описание')
	image = forms.ImageField(label='Постер')
	tags = forms.CharField(label='Тэги')
	members = forms.MultipleChoiceField(label='Участники', choices=members)


class BandUpdateForm(ModelForm):

	name = forms.CharField(label='Название')
	description = forms.CharField(label='Описание')
	image = forms.ImageField(label='Постер')
	tags = forms.CharField(label='Тэги')
	members = forms.MultipleChoiceField(label='Участники', choices=members)

	class Meta:
		model = Band  
		fields = ('name', 'description', 'image', 'members')