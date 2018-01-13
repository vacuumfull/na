from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from place.models import Place


class PlaceModelForm(ModelForm):

    musicians = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(groups__name="Музыканты"),
        label='Музыканты', initial=0)

    class Meta:
        model = Place
        fields = ('title', 'description', 'address', 'coordinates',
                  'worktime', 'image', 'icon', 'musicians', 'tags')
