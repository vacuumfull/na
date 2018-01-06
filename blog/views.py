"""Blog view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from blog.forms import BlogForm
from blog.models import Blog
from tag.models import Tag


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


class BlogCreate(LoginRequiredMixin, CreateView):
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
        SEPARATOR = '|'
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        # create blog tags
        tags = set(self.request.POST.get('tags').split(SEPARATOR))
        for name in tags:
            if len(name) != 0: 
                obj, _created = Tag.objects.get_or_create(name=name.lower())
                obj.blog_tags.add(instance)
        return super().form_valid(form)



class BlogUpdate(LoginRequiredMixin, UpdateView):
    """Update blog post."""

    model = Blog
    fields = [
        'title', 'rubric', 'image', 'annotation', 'content', 'event', 'place']
    success_url = reverse_lazy('blog:list')


class BlogsUserView(LoginRequiredMixin, TemplateView):
    """Added by user blogs"""

    template_name = 'blog/blog_user_list.html'
