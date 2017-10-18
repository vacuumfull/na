"""Blog view."""
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from blog.models import Blog


class IndexList(ListView):
    """Index list for blogs."""

    queryset = Blog.objects.published()
    context_object_name = 'blogs'


class BlogView(DetailView):
    """Blog view class."""

    model = Blog


class BlogCreate(CreateView):
    """Create blog post."""

    model = Blog
    fields = [
        'title', 'rubric', 'image', 'annotation', 'content', 'event', 'place']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        """Add user info to form."""
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdate(UpdateView):
    """Update blog post."""

    model = Blog
    fields = [
        'title', 'rubric', 'image', 'annotation', 'content', 'event', 'place']
    success_url = reverse_lazy('blog:index')
