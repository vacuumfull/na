from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import Group


AUTH_GROUPS =  {"user": "Пользователи",
                "musician": "Музыканты",
                "deputy": "Представители",
                "organizer": "Организаторы"}



class SignupUser(FormView):
    """Signup view with default SignUp form."""

    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/'

    def form_valid(self, form):
        """Authenticate user after registration."""
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        group = Group.objects.get(name=AUTH_GROUPS.get(self.request.POST['status']))
        group.user_set.add(user)
        login(self.request, user)
        return super().form_valid(form)


class SettingsView(LoginRequiredMixin, TemplateView):

    template_name = 'member/settings.html'