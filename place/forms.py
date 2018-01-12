from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from place.models import Place


class PlaceModelForm(ModelForm):

    musicians = forms.MultipleChoiceField(
        label='Участники', choices=User.objects.values_list('id', 'username'))

    class Meta:
        model = Place
        fields = ('title', 'description', 'address', 'coordinates',
                  'worktime', 'image', 'icon', 'musicians', 'tags')
