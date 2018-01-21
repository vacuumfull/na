from django import forms
from django.forms import ModelForm

from ckeditor.fields import CKEditorWidget

from blog.models import RUBRICS_LIST, Blog
from event.models import Event
from place.models import Place


class BlogModelForm(ModelForm):

    rubric = forms.ChoiceField(
        label='Рубрика', choices=RUBRICS_LIST,
        widget=forms.Select(), required=True)
    place = forms.ModelChoiceField(
        queryset=Place.objects.published(), label='Место проведения', initial=0)
    event = forms.ModelChoiceField(
        queryset=Event.objects.published(), label='Событие', initial=0)

    class Meta:
        model = Blog
        fields = ('title', 'rubric', 'image', 'annotation', 'content',
                  'place', 'event', 'tags')

    def __init__(self, *args, **kwargs):
        super(BlogModelForm, self).__init__(*args, **kwargs)
        
        for key in self.fields:
            self.fields['place'].required = False
            self.fields['event'].required = False
