import django.contrib.auth.urls
from django.conf.urls import include, url

from member.views import LoginView

app_name = 'user'
urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^', include(django.contrib.auth.urls))
]
