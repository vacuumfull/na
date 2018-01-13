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
from place.forms import PlaceModelForm


class PlaceList(ListView):
    """Place with locations list"""

    queryset = Place.objects.published()
    context_object_name = 'places'
    paginate_by = 16


class PlaceView(DetailView):
    """Detail view places."""

    model = Place


class PlacesUserView(LoginRequiredMixin, TemplateView):
    """User places list"""

    template_name = 'place/place_user_list.html'


class PlaceCreate(LoginRequiredMixin, CreateView):
    """Create blog post."""

    form_class = PlaceModelForm
    model = Place
    success_url = reverse_lazy('place:list')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class PlaceUpdate(LoginRequiredMixin, UpdateView):
    """Update blog post."""

    form_class = PlaceModelForm
    model = Place
    success_url = reverse_lazy('place:list')
    template_name = 'place/place_update.html'

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class MapView(TemplateView):
    """Maps page"""

    template_name = 'place/place_map.html'