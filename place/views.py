"""Places with locations view."""
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


from place.models import Place


class PlaceList(ListView):
    """Place with locations list"""

    model = Place
    context_object_name = 'places'


class PlaceView(DetailView):
    """Detail view places."""

    model = Place


class PlaceCreate(CreateView):
    """Create blog post."""

    model = Place
    fields = ['title', 'description', 'musicians', 'image', 'icon']
    success_url = reverse_lazy('place:index')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)


class PlaceUpdate(UpdateView):
    """Update blog post."""

    model = Place
    fields = ['title', 'description', 'musicians', 'image', 'icon']
    success_url = reverse_lazy('place:index')


class MapView(TemplateView):
    """Maps page"""

    template_name = 'place/places_map.html'
