from django.urls import path, re_path

from blog.views import (IndexList, BlogCreate, BlogView, BlogUpdate, BlogsUserView)


app_name = 'blog'
urlpatterns = [
    path('', IndexList.as_view(), name='index'),
    re_path(r'^_rubrics/(?P<rubric>(imho|festivals|music))/$',
            IndexList.as_view(), name='rubric'),
    path('new/', BlogCreate.as_view(), name='create'),
    path('list/', BlogsUserView.as_view(), name='list'),
    path('<slug:slug>/', BlogView.as_view(), name='view'),
    path('<slug:slug>/edit/', BlogUpdate.as_view(), name='edit'),
]
