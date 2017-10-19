from django.conf.urls import url

from band.views import BandList, BandCreate, BandDetail, BandUpdate


app_name = 'band'
urlpatterns = [
    url(r'^$', BandList.as_view(), name='index'),
    url(r'^new/$', BandCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', BandDetail.as_view(), name='view'),
    url(r'^(?P<slug>[-\w]+)/edit/$', BandUpdate.as_view(), name='edit'),
]
