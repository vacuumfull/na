from django.forms import inlineformset_factory
from django import forms
from place.models import Location, Place
import datetime

class PlaceForm(forms.Form):
    pass

# Inline locatinos formset for place
LocationFormSet = inlineformset_factory(
    Place, Location, fields=('address', 'maps', 'worktime'), extra=1)
