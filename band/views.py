"""Band view generic."""
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from band.models import Band


class BandList(ListView):
    """Index list bands."""

    model = Band
    context_object_name = 'bands'


class BandDetail(DetailView):
    """Detail view for band."""

    model = Band


class BandCreate(CreateView):
    """Create band post."""

    model = Band
    fields = ['name', 'description', 'image', 'members']
    success_url = reverse_lazy('band:index')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super().form_valid(form)


class BandUpdate(UpdateView):
    """Update band post."""

    model = Band
    fields = ['name', 'description', 'image', 'members']
    success_url = reverse_lazy('band:index')


class BandsUserView(TemplateView):

    template_name = 'band/band_user_list.html'

    def dispath(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(BandsUserView, self).dispath(request, *args, **kwargs)
