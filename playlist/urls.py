from django.urls import path

from playlist.views import IndexList, PlaylistCreate, PlaylistView, PlaylistUpdate, PlaylistUserView

app_name = 'playlist'

urlpatterns = [
	path('', IndexList.as_view(), name='index'),
	path('new/', PlaylistCreate.as_view(), name='create'),
	path('list/', PlaylistUserView.as_view(), name='list'),
	path('<slug:slug>', PlaylistView.as_view(), name='view'),
	path('<slug:slug>/edit/', PlaylistUpdate.as_view(), name='update'),
]
