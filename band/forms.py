from django import forms
from django.contrib.auth.models import User

queryset = User.objects.values('id', 'username')
members = [(q['id'], q['username']) for q in queryset]

class BandForm(forms.Form):
	"""Band Form"""
	name = forms.CharField(label='Название')
	description = forms.CharField(label='Описание')
	image = forms.ImageField(label='Постер')
	tags = forms.CharField(label='Тэги')
	members = forms.MultipleChoiceField(label='Участники', choices=members)