from django.urls import include, path

from api import views


message_patterns = ([
    path('', views.send_message),
    path('remove/', views.remove_message),
    path('read/', views.read_messages),
    path('dialogs/<str:sessionid>/', views.get_dialogs),
    path('history/<int:dialog>/<str:sessionid>/<int:offset>',
         views.get_messages_history),
])

search_patterns = ([
    path('default/<str:keyword>/', views.search_default),
    path('type/<str:app>/<str:keyword>/', views.search_type),
    path('fast/<str:keyword>/', views.search_tags),
    path('tags/', views.get_tags)
])

place_patterns = ([
    path('list/<str:app>/<str:sessionid>/', views.list_items),
    path('remove/', views.remove_item)
])

urlpatterns = [
    # user info
    path('1/users/<str:sessionid>/', views.get_users),
    # comments
    path('1/comment/<str:app>/<int:key>/<int:offset>/',
         views.get_comment),
    path('1/send/', views.send_comment),
    # rating
    path('1/rating/<str:app>/<int:key>/<str:sessionid>/',
         views.get_rating),
    path('1/rating/<int:key>/<str:app>/', views.get_rate_unlogin), 
    path('1/vote/', views.vote_rating),

    path('1/message/', include(message_patterns)),
    path('1/search/', include(search_patterns)),
    path('1/item/', include(place_patterns))
]
