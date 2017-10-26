from django.conf.urls import url

from blog.views import (IndexList, BlogCreate, BlogView, BlogUpdate,
                        get_blog_rating)

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexList.as_view(), name='index'),
    url(r'^_rubrics/(?P<rubric>(imho|festivals|music))/$',
        IndexList.as_view(), name='rubric'),
    url(r'^new/$', BlogCreate.as_view(), name='create'),
    url(r'^rating/(?P<sessionid>(.*))/(?P<blog_id>\d+)/$', get_blog_rating),
    url(r'^(?P<slug>[-\w]+)/$', BlogView.as_view(), name='view'),
    url(r'^(?P<slug>[-\w]+)/edit/$', BlogUpdate.as_view(), name='edit'),
]
