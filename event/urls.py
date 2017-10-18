from django.conf.urls import url

from event.views import EventList, EventCreate, EventView, EventUpdate


app_name = 'event'
urlpatterns = [
    url(r'^$', EventList.as_view(), name='index'),
    url(r'^new/$', EventCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', EventView.as_view(), name='view'),
    url(r'^(?P<slug>[-\w]+)/edit/$', EventUpdate.as_view(), name='edit'),
]
