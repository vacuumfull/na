from django.urls import path
from django.contrib.auth.views import LoginView, logout

from member.views import SignupUser


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout, name='logout', kwargs={'next_page': '/'}),
    path('signup/', SignupUser.as_view(), name='signup')
]
