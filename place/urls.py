from django.conf.urls import url

from place.views import PlaceList, PlaceView


app_name = 'place'
urlpatterns = [
    url(r'(?P<slug>[-\w]+)/$', PlaceView.as_view(), name='view'),
    url(r'^$', PlaceList.as_view(), name='index'),
]
