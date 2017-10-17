from django.conf.urls import url

from blog.views import IndexList, BlogCreate, BlogView

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexList.as_view(), name='index'),
    url(r'^new/$', BlogCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', BlogView.as_view(), name='view'),
]
