"""Band view generic."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from band.models import Band
from band.forms import BandModelForm

class BandList(ListView):
    """Index list bands."""

    model = Band
    context_object_name = 'bands'
    paginate_by = 16


class BandDetail(DetailView):
    """Detail view for band."""

    model = Band


class BandCreate(LoginRequiredMixin, CreateView):
    """Create band post."""

    form_class = BandModelForm
    model = Band
    success_url = reverse_lazy('band:list')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class BandUpdate(LoginRequiredMixin, UpdateView):
    """Update band post."""

    form_class = BandModelForm
    model = Band
    success_url = reverse_lazy('band:index')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class BandsUserView(LoginRequiredMixin, TemplateView):
    """WTF docstring? Maybe this ListView class-based?"""

    template_name = 'band/band_user_list.html'
