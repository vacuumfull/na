"""Places with locations view."""
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from place.models import Place


class PlaceList(ListView):
    """Place with locations list"""

    model = Place
    context_object_name = 'places'


class PlaceView(DetailView):
    """Detail view places."""

    model = Place


class MapView(TemplateView):
    """Maps page"""

    template_name = 'place/places_map.html'