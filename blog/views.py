"""Blog view."""
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django import forms
from django.shortcuts import redirect

from blog.models import Blog, BlogForm
from place.models import Place


class IndexList(ListView):
    """Index list for blogs."""

    queryset = Blog.objects.published()
    context_object_name = 'blogs'

    def get_queryset(self):
        """Filter queryset if choise one rubric."""
        query = super().get_queryset()
        if 'rubric' in self.kwargs:
            query = query.filter(rubric=self.kwargs['rubric'])
        return query


class BlogView(DetailView):
    """Blog view class."""

    model = Blog


class BlogCreate(CreateView):
    """Create blog post."""

    model = Blog
    fields = ['title', 'rubric', 'image', 'annotation', 'content', 'event', 'place']
    success_url = reverse_lazy('blog:list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogForm
        return context

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.author = self.request.user
        form.author = self.request.user
        return super().form_valid(form)


class BlogUpdate(UpdateView):
    """Update blog post."""

    model = Blog
    fields = [
        'title', 'rubric', 'image', 'annotation', 'content', 'event', 'place']
    success_url = reverse_lazy('blog:list')


class BlogsUserView(TemplateView):
    """Added by user blogs"""

    template_name = 'blog/blog_user_list.html'

    def dispath(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return super(BlogsUserView, self).dispath(request, *args, **kwargs)
