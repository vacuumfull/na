from django.conf.urls import url

from flatten.views import ContactsView, ThanksView, RulesView

app_name = 'flatten'
urlpatterns = [
    url(r'contacts/$', ContactsView.as_view(), name='contacts'),
    url(r'thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'rules/$', RulesView.as_view(), name='rules'),
]
