from django.urls import path
from oauth.views import autorize, testcallback


app_name = 'oauth'
urlpatterns = [
    path('testoauth', autorize, name='oauth-google'),
	path('callback', testcallback),
]