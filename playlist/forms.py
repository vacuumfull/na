from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from playlist.models import Playlist


class PlaylistModelForm(ModelForm):


	class Meta:
		model = Playlist
		fields = ('name', 'annotation', 'content','image', 'tags')


	def __init__(self, *args, **kwargs):
		super(PlaylistModelForm, self).__init__(*args, **kwargs)
		
		for key in self.fields:
			self.fields['image'].required = False
