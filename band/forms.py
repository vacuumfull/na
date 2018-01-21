from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from band.models import Band


class BandModelForm(ModelForm):
    
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(groups__name="Музыканты"),
        label='Музыканты', initial=0)

    class Meta:
        model = Band
        fields = ('name', 'description', 'image', 'members', 'tags')
