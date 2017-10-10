"""Places with locations view."""
from django.views.generic.detail import DetailView

from place.models import Place


class PlaceView(DetailView):
    """Detail view places."""

    model = Place
