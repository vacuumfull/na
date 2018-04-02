"""under URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.urls import include, path, re_path
from django.conf.urls import handler404, handler500
from flatten.views import get_sitemap

import api.urls
import band.urls
import blog.urls
import event.urls
import flatten.urls
import member.urls
import place.urls
import playlist.urls
import oauth.urls
from under.views import IndexView

handler404 = 'under.views.handler404'
handler500 = 'under.views.handler404'

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(api.urls)),
	path('bands/', include(band.urls)),
	path('blogs/', include(blog.urls)),
	path('events/', include(event.urls)),
	path('places/', include(place.urls)),
	path('page/', include(flatten.urls)),
	path('playlists/', include(playlist.urls)),
	path('auth/', include(oauth.urls)),
	
	re_path(r'^', include(member.urls)),
	path('', IndexView.as_view(), name='index'),
	path('sitemap.xml', get_sitemap)
]

# Add media path to media directory
urlpatterns += [
	re_path(r'^media/(?P<path>.*)$', serve,
			 {'document_root': settings.MEDIA_ROOT})
]