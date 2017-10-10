from django.conf.urls import url

from event.views import EventList, EventView


app_name = 'event'
urlpatterns = [
    url(r'(?P<slug>[-\w]+)/$', EventView.as_view(), name='view'),
    url(r'^$', EventList.as_view(), name='index'),
]
