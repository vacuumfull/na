"""Places with locations view."""
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from place.models import Place
from place.forms import LocationFormSet


class PlaceList(ListView):
    """Place with locations list"""

    queryset = Place.objects.published()
    context_object_name = 'places'


class PlaceView(DetailView):
    """Detail view places."""

    model = Place


class PlacesUserView(TemplateView):
    """User places list"""

    template_name = 'place/place_user_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(PlacesUserView, self).dispatch(request, *args, **kwargs)


class PlaceCreate(CreateView):
    """Create blog post."""

    model = Place
    fields = ['title', 'description', 'musicians', 'image', 'icon']
    success_url = reverse_lazy('place:index')

    def form_valid(self, form):
        """Add locations formset to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user

        location_formset = LocationFormSet(
            self.request.POST, instance=instance)
        if location_formset.is_valid():
            instance.save()
            location_formset.save()
            return HttpResponseRedirect(reverse_lazy('place:index'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.POST:
            context['location_formset'] = LocationFormSet(self.request.POST)
        else:
            context['location_formset'] = LocationFormSet()
        return context


class PlaceUpdate(UpdateView):
    """Update blog post."""

    model = Place
    fields = ['title', 'description', 'musicians', 'image', 'icon']
    success_url = reverse_lazy('place:index')

    def form_valid(self, form):
        """Update locations formset to form."""
        instance = form.save(commit=False)

        location_formset = LocationFormSet(
            self.request.POST, instance=instance)
        if location_formset.is_valid():
            instance.save()
            location_formset.save()
            return HttpResponseRedirect(reverse_lazy('place:index'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.POST:
            context['location_formset'] = LocationFormSet(self.request.POST)
        else:
            context['location_formset'] = LocationFormSet(instance=self.object)
        return context


class MapView(TemplateView):
    """Maps page"""

    template_name = 'place/place_map.html'
