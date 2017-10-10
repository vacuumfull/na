"""Event view."""
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from event.models import Event


class EventList(ListView):
    """Index list for events."""

    model = Event
    context_object_name = 'events'


class EventView(DetailView):
    """Event details view."""

    model = Event
