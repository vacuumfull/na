from django.conf.urls import url

from place.views import PlaceList, PlaceView, MapView


app_name = 'place'
urlpatterns = [
    url(r'^map/$', MapView.as_view(), name='map'),
    url(r'(?P<slug>[-\w]+)/$', PlaceView.as_view(), name='view'),
    url(r'^$', PlaceList.as_view(), name='index')
]
