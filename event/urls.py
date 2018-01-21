from django.urls import path

from event.views import EventList, EventCreate, EventView, EventUpdate, EventsUserView


app_name = 'event'
urlpatterns = [
    path('', EventList.as_view(), name='index'),
    path('new/', EventCreate.as_view(), name='create'),
    path('list/', EventsUserView.as_view(), name='list'),
    path('<slug:slug>/', EventView.as_view(), name='view'),
    path('<slug:slug>/edit/', EventUpdate.as_view(), name='edit'),
]
