"""Blog view."""
from django.core.urlresolvers import reverse_lazy
from django.http.response import JsonResponse
from django.views.decorators.http import require_GET
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.sessions.backends.db import SessionStore

from blog.models import Blog, Rating, User


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


@require_GET
def get_blog_rating(request, sessionid, blog_id: int):
    """Get average blog rating."""
    session = SessionStore(sessionid)
    try:
        user = User.objects.get(id=session.get('_auth_user_id'))
    except User.DoesNotExist:
        user = None
    result = Rating.objects.average(blog_id, user)
    return JsonResponse(result)


# def vote_blog_rating(request, blog)
