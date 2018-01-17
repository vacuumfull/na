"""Blog view."""
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from itertools import chain
import json

from blog.forms import BlogModelForm
from blog.models import Blog
from member.models import UserExtend

class IndexList(ListView):
    """Index list for blogs."""

    queryset = Blog.objects.published()
    context_object_name = 'blogs'
    paginate_by = 16

    def get_queryset(self):
        """Filter queryset if choise one rubric."""
        query = super().get_queryset()
        #if self.request.user.is_authenticated:
            # Здесь нужно подумать над выводом того, что нравится пользователю
           # stylesset = UserExtend.objects.filter(user_id=self.request.user.id).values('prefer_styles')
           # styles = json.loads(stylesset[0]['prefer_styles'])
           # query_styles = query.select_related().all()
           # tags = Tag.objects.filter(name__in=styles).get()
           # blogs = tags.blog_tags.all()
        #else:
        if 'rubric' in self.kwargs:
            query = query.filter(rubric=self.kwargs['rubric'])
        return query.order_by('created_at').reverse()


class BlogView(DetailView):
    """Blog view class."""

    model = Blog


class BlogCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create blog post."""

    permission_required = 'blog.add_blog'
    form_class = BlogModelForm
    model = Blog
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class BlogUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Update blog post."""

    permission_required = 'blog.change_blog'
    form_class = BlogModelForm
    model = Blog
    success_url = reverse_lazy('blog:index')
    template_name = 'blog/blog_update.html'

    def get_object(self, queryset=None):
        """Return 404 if user not owner object."""
        return get_object_or_404(
            self.model, slug=self.kwargs["slug"], author=self.request.user)

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


class BlogDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Delete blog post."""

    permission_required = 'blog.delete_blog'
    model = Blog
    success_url = reverse_lazy('blog:index')


class BlogsUserView(LoginRequiredMixin, TemplateView):
    """Added by user blogs"""

    template_name = 'blog/blog_user_list.html'
