from django import forms
from django.forms import ModelForm

from ckeditor.fields import CKEditorWidget

from blog.models import Blog
from blog.models import RUBRICS_LIST
from event.models import Event
from place.models import Place

class BlogForm(forms.Form):

    title = forms.CharField(label='Название')
    image = forms.ImageField(label='Изображение')
    annotation = forms.CharField(label='Аннотация')
    tags = forms.CharField(label='Тэги')
    rubric = forms.ChoiceField(label='Рубрика', widget=forms.Select(), choices=RUBRICS_LIST, required=True)
    content = forms.CharField(label='Содержание', widget=CKEditorWidget)
    place = forms.ModelChoiceField(queryset=Place.objects.published(), label='Место проведения')
    event = forms.ModelChoiceField(queryset=Event.objects.upcoming(), label='Событие')


class BlogUpdateForm(ModelForm):

    title = forms.CharField(label='Название')
    image = forms.ImageField(label='Изображение')
    annotation = forms.CharField(label='Аннотация')
    tags = forms.CharField(label='Тэги', widget=forms.TextInput(attrs={'class':'form-control'}))
    rubric = forms.ChoiceField(label='Рубрика', widget=forms.Select(), choices=RUBRICS_LIST, required=True)
    content = forms.CharField(label='Содержание', widget=CKEditorWidget)
    place = forms.ModelChoiceField(queryset=Place.objects.published(), label='Место проведения')
    event = forms.ModelChoiceField(queryset=Event.objects.upcoming(), label='Событие')

    class Meta:
        model = Blog  
        fields = ('title', 'rubric', 'image', 'annotation', 'content', 'event', 'place', 'tags')
