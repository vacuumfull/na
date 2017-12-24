"""Event view."""
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

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
    success_url = reverse_lazy('event:list')

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


class EventsUserView(TemplateView):
    """User places list"""

    template_name = 'event/event_user_list.html'

    def dispath(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(EventsUserView, self).dispath(request, *args, **kwargs)

