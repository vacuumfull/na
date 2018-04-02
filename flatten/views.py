from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader

def get_sitemap(request):
    xml_path = "flatten/templates/flatten/sitemap.xml"
    return HttpResponse(open(xml_path).read(), content_type='text/xml')


class ContactsView(TemplateView):
    """Contacts static pages."""

    template_name = 'flatten/contacts.html'


class ThanksView(TemplateView):
    """Thanks page."""

    template_name = 'flatten/thanks.html'


class RulesView(TemplateView):
    """Rules page."""

    template_name = 'flatten/rules.html'


class SearchView(TemplateView):
    """Search page"""

    template_name = 'flatten/search.html'
