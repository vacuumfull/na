from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


from band.models import Band
from place.models import Place
from event.models import Event


class EventModelForm(ModelForm):

    musicians = forms.ModelChoiceField(
        queryset=User.objects.filter(is_superuser=False, is_staff=False, is_active=True),
        label='Музыканты')
    bands = forms.ModelChoiceField(
        queryset=Band.objects.published(), label='Коллективы')
    locations = forms.ModelChoiceField(
        queryset=Place.objects.all(), label='Заведения')

    class Meta:
        model = Event
        fields = ('title', 'image', 'description', 'date', 'price',
                  'musicians', 'bands', 'locations', 'tags')
