from django.conf.urls import url
from django.contrib.auth.views import LoginView, logout

from member.views import SignupUser

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^signup/$', SignupUser.as_view(), name='signup')
]
