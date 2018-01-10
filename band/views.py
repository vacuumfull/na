"""Band view generic."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from band.models import Band
from band.forms import BandForm 
from tag.models import Tag

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

    model = Band
    fields = ['name', 'description', 'image', 'members']
    success_url = reverse_lazy('band:list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BandForm
        return context

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
                obj.band_tags.add(instance)
        return super().form_valid(form)


class BandUpdate(LoginRequiredMixin, UpdateView):
    """Update band post."""

    model = Band
    fields = ['name', 'description', 'image', 'members']
    success_url = reverse_lazy('band:index')

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
                obj.band_tags.add(instance)
        return super().form_valid(form)


class BandsUserView(LoginRequiredMixin, TemplateView):

    template_name = 'band/band_user_list.html'