from django.forms import inlineformset_factory, ModelForm
from django import forms
from place.models import Location, Place
from django.contrib.auth.models import User

queryset = User.objects.values('id', 'username')
musicians = [(q['id'], q['username']) for q in queryset]

class PlaceForm(forms.Form):
    """Place form"""
    title = forms.CharField(label='Название')
    description = forms.CharField(label='Описание')
    coordinates = forms.CharField(label='Координаты')
    worktime = forms.CharField(label='Время работы')
    address = forms.CharField(label='Адрес')
    image = forms.ImageField(label='Изображение')
    icon = forms.ImageField(label='Иконка')
    tags = forms.CharField(label='Тэги')	
    musicians = forms.MultipleChoiceField(label='Участники', choices=musicians)

# Inline locatinos formset for place
#LocationFormSet = inlineformset_factory(
#    Place, Location, fields=('address', 'maps', 'worktime'), extra=1)


class PlaceUpdateForm(ModelForm):

    title = forms.CharField(label='Название')
    description = forms.CharField(label='Описание')
    coordinates = forms.CharField(label='Координаты')
    worktime = forms.CharField(label='Время работы')
    address = forms.CharField(label='Адрес')
    image = forms.ImageField(label='Изображение')
    icon = forms.ImageField(label='Иконка')
    tags = forms.CharField(label='Тэги')	

    class Meta:
        model = Place
        fields = ('title', 'description', 'address', 'coordinates', 'worktime', 'musicians', 'image', 'icon', 'tags')
