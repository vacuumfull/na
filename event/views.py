"""Event view."""
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
import json
from event.models import Event
from event.forms import EventModelForm
from member.models import UserExtend


class EventList(ListView):
    """Index list for events."""

    queryset = Event.objects.upcoming()
    context_object_name = 'events'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            styles = UserExtend.objects.filter(user=self.request.user).values('prefer_styles')
            if styles[0]['prefer_styles'] is not None:
                context['prefered'] = Event.objects.filter(published=True, tags__name__in=json.loads(styles[0]['prefer_styles'])).distinct()
        return context


class EventView(DetailView):
    """Event details view."""

    model = Event


class EventCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create event."""

    permission_required = 'event.add_event'
    form_class = EventModelForm
    model = Event
    success_url = reverse_lazy('event:list')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        print(form['bands'])
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class EventUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Update blog post."""

    permission_required = 'event.change_event'
    form_class = EventModelForm
    model = Event
    success_url = reverse_lazy('event:list')
    template_name = 'event/event_update.html'

    def get_object(self, queryset=None):
        """Return 404 if user not owner object."""
        return get_object_or_404(
            self.model, slug=self.kwargs["slug"], owner=self.request.user)

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class EventDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete event post."""

    permission_required = 'event.delete_event'
    model = Event
    success_url = reverse_lazy('event:index')


class EventsUserView(LoginRequiredMixin, TemplateView):
    """User places list"""

    template_name = 'event/event_user_list.html'
