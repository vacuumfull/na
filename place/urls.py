from django.conf.urls import url

from place.views import PlaceView


app_name = 'place'
urlpatterns = [
    url(r'(?P<slug>[-\w]+)/$', PlaceView.as_view(), name='view'),
]
