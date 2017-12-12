from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^1/comment/(?P<app>\w+)/(?P<key>\d+)/(?P<sessionid>.*)/' +
        '(?P<offset>\d+)/$',
        views.get_comment),
    url(r'^1/rating/(?P<app>\w+)/(?P<key>\d+)/(?P<sessionid>.*)/$',
        views.get_rating),
    url(r'^1/users/(?P<sessionid>.*)/$', views.get_users),
    url(r'^1/send/$', views.send_comment),
    url(r'^1/vote/$', views.vote_rating),

    url(r'^1/message/$', views.send_message),
    url(r'^1/message/remove/$', views.remove_message),
    
    url(r'^1/messages/read/$', views.read_messages),

    url(r'^1/messages/dialogs/(?P<sessionid>.*)/$', views.get_dialogs),

    url(r'^1/messages/history/(?P<dialog>\d+)/(?P<sessionid>.*)/' +
        '(?P<offset>\d+)/$', views.get_messages_history),

    url(r'^1/search/default/(?P<keyword>.*)/$', views.search_default),

    url(r'^1/search/type/(?P<app>\w+)/(?P<keyword>.*)/$', views.search_type),

    url(r'^1/search/fast/(?P<keyword>.*)/$', views.search_tags),

    url(r'^1/search/tags/$', views.get_tags)
    
]
