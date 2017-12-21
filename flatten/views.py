from django.views.generic import TemplateView


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