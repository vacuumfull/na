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

from playlist.models import Playlist
from playlist.forms import PlaylistModelForm
from member.models import UserExtend


class IndexList(ListView):
    """Index list for blogs."""

    queryset = Playlist.objects.published()
    context_object_name = 'playlists'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            styles = UserExtend.objects.filter(user=self.request.user).values('prefer_styles')
            context['prefered'] = Playlist.objects.filter(published=True, tags__name__in=json.loads(styles[0]['prefer_styles'])).distinct()
        return context


class PlaylistView(DetailView):
	"""Playlist view class."""
	model = Playlist


class PlaylistCreate(LoginRequiredMixin, CreateView):
	"""Create playlist"""

	form_class = PlaylistModelForm
	model = Playlist
	success_url = reverse_lazy('playlist:list')

	def form_valid(self, form):
		"""Add user info to form."""
		instance = form.save(commit=False)
		instance.creator = self.request.user
		instance.save()
		form.save_m2m()
		return super().form_valid(form)


class PlaylistUpdate(LoginRequiredMixin, UpdateView):
    """Update blog post."""

    permission_required = 'blog.change_blog'
    form_class = PlaylistModelForm
    model = Playlist
    success_url = reverse_lazy('playlist:list')
    template_name = 'playlist/playlist_update.html'

    def get_object(self, queryset=None):
        """Return 404 if user not owner object."""
        return get_object_or_404(
            self.model, slug=self.kwargs["slug"], creator=self.request.user)

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.creator = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class PlaylistUserView(LoginRequiredMixin, TemplateView):
    """User places list"""

    template_name = 'playlist/playlist_user_list.html'

class PlaylistDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete playlist."""

    permission_required = 'playlist.delete_playlist'
    model = Playlist
    success_url = reverse_lazy('playlist:index')