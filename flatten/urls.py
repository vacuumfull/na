from django.urls import path

from flatten.views import ContactsView, ThanksView, RulesView, SearchView


app_name = 'flatten'
urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('rules/', RulesView.as_view(), name='rules'),
    path('search/', SearchView.as_view(), name='search')
]
