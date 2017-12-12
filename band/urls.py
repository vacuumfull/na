from django.urls import path

from band.views import BandList, BandCreate, BandDetail, BandUpdate


app_name = 'band'
urlpatterns = [
    path('', BandList.as_view(), name='index'),
    path('new/', BandCreate.as_view(), name='create'),
    path('<slug:slug>/', BandDetail.as_view(), name='view'),
    path('<slug:slug>/edit/', BandUpdate.as_view(), name='edit'),
]
