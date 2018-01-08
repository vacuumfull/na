"""Places with locations view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from place.models import Place
from place.forms import PlaceForm
from tag.models import Tag


class PlaceList(ListView):
    """Place with locations list"""

    queryset = Place.objects.published()
    context_object_name = 'places'


class PlaceView(DetailView):
    """Detail view places."""

    model = Place


class PlacesUserView(LoginRequiredMixin, TemplateView):
    """User places list"""

    template_name = 'place/place_user_list.html'


class PlaceCreate(LoginRequiredMixin, CreateView):
    """Create blog post."""

    model = Place
    fields = ['title', 'description', 'address', 'coordinates', 'worktime', 'musicians', 'image', 'icon']
    success_url = reverse_lazy('place:list')

    def form_valid(self, form):
        """Add user info to form."""
        SEPARATOR = '|'
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        # create blog tags
        tags = set(self.request.POST.get('tags').split(SEPARATOR))
        for name in tags:
            if len(name) != 0: 
                obj, _created = Tag.objects.get_or_create(name=name.lower())
                obj.place_tags.add(instance)
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PlaceForm
        return context


class PlaceUpdate(LoginRequiredMixin, UpdateView):
    """Update blog post."""

    model = Place
    fields = ['title', 'description', 'address', 'coordinates', 'worktime', 'musicians', 'image', 'icon', 'tags']
    success_url = reverse_lazy('place:index')

    def form_valid(self, form):
        """Add user info to form."""
        SEPARATOR = '|'
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        # create blog tags
        tags = set(self.request.POST.get('tags').split(SEPARATOR))
        for name in tags:
            if len(name) != 0: 
                obj, _created = Tag.objects.get_or_create(name=name.lower())
                obj.place_tags.add(instance)
        return super().form_valid(form)


class MapView(TemplateView):
    """Maps page"""

    template_name = 'place/place_map.html'
