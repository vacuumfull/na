from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


from band.models import Band
from place.models import Place
from event.models import Event


class EventModelForm(ModelForm):

    musicians = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(groups__name="Музыканты"),
        label='Музыканты', initial=0)
    bands = forms.ModelChoiceField(
        queryset=Band.objects.published(), label='Коллективы')
    locations = forms.ModelChoiceField(
        queryset=Place.objects.published(), label='Заведения', initial=0)

    class Meta:
        model = Event
        fields = ('title', 'image', 'description', 'date', 'price',
                  'musicians', 'bands', 'locations', 'tags')


    def __init__(self, *args, **kwargs):
        super(EventModelForm, self).__init__(*args, **kwargs)
        
        for key in self.fields:
            self.fields['musicians'].required = False
            self.fields['bands'].required = False
            self.fields['locations'].required = False
