"""Places with locations view."""
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from place.models import Place


class PlaceList(ListView):
    """Place with locations list"""

    model = Place
    context_object_name = 'places'


class PlaceView(DetailView):
    """Detail view places."""

    model = Place
