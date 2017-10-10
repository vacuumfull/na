"""Band view generic."""
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from band.models import Band


class BandList(ListView):
    """Index list bands."""

    model = Band
    context_object_name = 'bands'


class BandDetail(DetailView):
    """Detail view for band."""

    model = Band
