from django.urls import path
from oauth.views import autorize, callback, test


app_name = 'oauth'
urlpatterns = [
    path('google/auth', autorize, name='oauth-google'),
	path('google/callback', callback),
	path('google/test', test),
]