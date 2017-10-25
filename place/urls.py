from django.conf.urls import url

from place.views import PlaceCreate, PlaceList, PlaceUpdate, PlaceView, MapView


app_name = 'place'
urlpatterns = [
    url(r'^$', PlaceList.as_view(), name='index'),
    url(r'^map/$', MapView.as_view(), name='map'),
    url(r'^new/$', PlaceCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', PlaceView.as_view(), name='view'),
    url(r'^(?P<slug>[-\w]+)/edit/$', PlaceUpdate.as_view(), name='edit'),
    
]
