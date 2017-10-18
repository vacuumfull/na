"""Event view."""
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from event.models import Event


class EventList(ListView):
    """Index list for events."""

    queryset = Event.objects.upcoming()
    context_object_name = 'events'


class EventView(DetailView):
    """Event details view."""

    model = Event


class EventCreate(CreateView):
    """Create blog post."""

    model = Event
    fields = ['title', 'image', 'description', 'date', 'price',
              'bands', 'musicians', 'locations']
    success_url = reverse_lazy('event:index')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)


class EventUpdate(UpdateView):
    """Update blog post."""

    model = Event
    fields = ['title', 'image', 'description', 'date', 'price',
              'bands', 'musicians', 'locations']
    success_url = reverse_lazy('event:index')
