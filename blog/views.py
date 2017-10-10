"""Blog view."""
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models import Blog


class IndexList(ListView):
    """Index list for blogs."""

    model = Blog
    context_object_name = 'blogs'


class BlogView(DetailView):
    """Blog view class."""

    model = Blog
