"""Band view generic."""
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

import json

from band.models import Band
from band.forms import BandModelForm
from member.models import UserExtend

class BandList(ListView):
    """Index list bands."""

    model = Band
    context_object_name = 'bands'
    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            styles = UserExtend.objects.filter(user=self.request.user).values('prefer_styles')
            if styles[0]['prefer_styles'] is not None:
                context['prefered'] = Band.objects.filter(published=True, tags__name__in=json.loads(styles[0]['prefer_styles'])).distinct()
        return context


class BandDetail(DetailView):
    """Detail view for band."""

    model = Band


class BandCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create band post."""

    permission_required = 'band.add_band'
    form_class = BandModelForm
    model = Band
    success_url = reverse_lazy('band:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True
        return context

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class BandUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Update band post."""

    permission_required = 'band.change_band'
    form_class = BandModelForm
    model = Band
    success_url = reverse_lazy('band:index')

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


class BandDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete band post."""

    permission_required = 'band.delete_band'
    model = Band
    success_url = reverse_lazy('band:index')


class BandsUserView(LoginRequiredMixin, TemplateView):
    """WTF docstring? Maybe this ListView class-based?"""

    template_name = 'band/band_user_list.html'
