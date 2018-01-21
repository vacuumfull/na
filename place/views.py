"""Places with locations view."""
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

import json

from place.models import Place
from place.forms import PlaceModelForm
from member.models import UserExtend


class PlaceList(ListView):
    """Place with locations list"""

    queryset = Place.objects.published()
    context_object_name = 'places'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            styles = UserExtend.objects.filter(user=self.request.user).values('prefer_styles')
            if styles[0]['prefer_styles'] is not None:
                context['prefered'] = Place.objects.filter(published=True, tags__name__in=json.loads(styles[0]['prefer_styles'])).distinct()
        return context


class PlaceView(DetailView):
    """Detail view places."""

    model = Place


class PlacesUserView(LoginRequiredMixin, TemplateView):
    """User places list"""

    template_name = 'place/place_user_list.html'


class PlaceCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create blog post."""

    permission_required = 'place.add_place'
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


class PlaceUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Update blog post."""

    permission_required = 'place.change_place'
    form_class = PlaceModelForm
    model = Place
    success_url = reverse_lazy('place:list')
    template_name = 'place/place_update.html'

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


class PlaceDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete place post."""

    permission_required = 'place.delete_place'
    model = Place
    success_url = reverse_lazy('place:index')


class MapView(TemplateView):
    """Maps page"""

    template_name = 'place/place_map.html'
