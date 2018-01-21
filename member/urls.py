from django.urls import path
from django.contrib.auth.views import LoginView, logout

from member.views import SignupUser, SettingsView, UserView


urlpatterns = [
    path('settings/', SettingsView.as_view(), name='settings'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout', kwargs={'next_page': '/'}),
    path('signup/', SignupUser.as_view(), name='signup'),
    path('member/<str:username>/', UserView.as_view(), name='userpage')
]
