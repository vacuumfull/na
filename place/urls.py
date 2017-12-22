from django.urls import path

from place.views import PlaceCreate, PlaceList, PlaceUpdate, PlaceView, PlacesUserView, MapView


app_name = 'place'
urlpatterns = [
    path('', PlaceList.as_view(), name='index'),
    path('map/', MapView.as_view(), name='map'),
    path('new/', PlaceCreate.as_view(), name='create'),
    path('list/', PlacesUserView.as_view(), name='list'),
    path('<slug:slug>/', PlaceView.as_view(), name='view'),
    path('<slug:slug>/edit/', PlaceUpdate.as_view(), name='edit'),
]
