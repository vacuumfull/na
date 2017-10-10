from django.conf.urls import url

from band.views import BandList, BandDetail


app_name = 'band'
urlpatterns = [
    url(r'(?P<slug>[-\w]+)/$', BandDetail.as_view(), name='view'),
    url(r'^$', BandList.as_view(), name='index'),
]
