from django.urls import path
from oauth.views import authorize, callback

app_name = 'oauth'
urlpatterns = [
	path('<str:app>/authorize', authorize),
	path('<str:app>/callback', callback)
]