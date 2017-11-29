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
    url(r'^1/messages/unread/(?P<sessionid>.*)/$', views.get_messages_unread),
    url(r'^1/messages/history/(?P<dialog>\d+)/(?P<sessionid>.*)/' +
        '(?P<offset>\d+)/$', views.get_messages_history),
]
