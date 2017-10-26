from django.forms import inlineformset_factory

from place.models import Location, Place


# Inline locatinos formset for place
LocationFormSet = inlineformset_factory(
    Place, Location, fields=('address', 'maps', 'worktime'), extra=1)
