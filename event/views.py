"""Event view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from event.models import Event
from event.forms import EventForm, EventUpdateForm
from tag.models import Tag


class EventList(ListView):
    """Index list for events."""

    queryset = Event.objects.upcoming()
    context_object_name = 'events'
    paginate_by = 16 


class EventView(DetailView):
    """Event details view."""

    model = Event


class EventCreate(LoginRequiredMixin, CreateView):
    """Create event."""

    model = Event
    fields = ['title', 'image', 'description', 'date', 'price','tags',
              'bands', 'musicians', 'locations']
    success_url = reverse_lazy('event:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventForm
        return context

    def form_valid(self, form):
        """Add user info to form."""
        SEPARATOR = '|'
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        # create event tags
        tags = set(self.request.POST.get('tags').split(SEPARATOR))
        for name in tags:
            if len(name) != 0: 
                obj, _created = Tag.objects.get_or_create(name=name.lower())
                obj.event_tags.add(instance)
        
        return super().form_valid(form)


class EventUpdate(LoginRequiredMixin, UpdateView):
    """Update blog post."""

    model = Event
    form_class = EventUpdateForm
    success_url = reverse_lazy('event:index')
    template_name = 'event/event_update.html'

    def form_valid(self, form):
        """Add user info to form."""
        SEPARATOR = '|'
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        # create event tags
        tags = set(self.request.POST.get('tags').split(SEPARATOR))
        for name in tags:
            if len(name) != 0: 
                obj, _created = Tag.objects.get_or_create(name=name.lower())
                obj.event_tags.add(instance)
        
        return super().form_valid(form)


class EventsUserView(LoginRequiredMixin, TemplateView):
    """User places list"""

    template_name = 'event/event_user_list.html'