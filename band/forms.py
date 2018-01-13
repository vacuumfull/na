from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from band.models import Band


class BandModelForm(ModelForm):
    members = forms.MultipleChoiceField(
        label='Участники', choices=User.objects.values_list('id', 'username'))

    class Meta:
        model = Band
        fields = ('name', 'description', 'image', 'members', 'tags')
