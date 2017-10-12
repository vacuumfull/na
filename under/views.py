from django.views.generic import TemplateView

from blog.models import Blog
from event.models import Event
from place.models import Place


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blogs'] = Blog.objects.last_blog()
        context['events'] = Event.objects.all()[:4]
        context['places'] = Place.objects.all()[:4]
        return context
