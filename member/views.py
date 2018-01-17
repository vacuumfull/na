from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import Group, User
from event.models import Event
from blog.models import Blog
from band.models import Band
from place.models import Place



AUTH_GROUPS =  {"user": "Пользователи",
                "musician": "Музыканты",
                "deputy": "Представители",
                "organizer": "Организаторы"}



class SignupUser(FormView):
    """Signup view with default SignUp form."""

    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/settings'

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



def get_user_profile(request, username):
    try:
        user = User.objects.get(username=username)

        blogs = None
        bands = None
        events = None
        places = None

        if user.is_superuser:
            return redirect('/')
        if user.groups.all()[0].name == "Пользователи":
            blogs = Blog.objects.filter(author=user)
        if user.groups.all()[0].name == "Музыканты":
            blogs = Blog.objects.filter(author=user)
            bands = Band.objects.filter(owner=user)
        if user.groups.all()[0].name == "Представители":
            blogs = Blog.objects.filter(author=user)
            places = Place.objects.filter(owner=user)
            bands = Band.objects.filter(owner=user)
        if user.groups.all()[0].name == "Организаторы":
            blogs = Blog.objects.filter(author=user)
            events = Event.objects.filter(owner=user)
  
        return render(request, 'member/userpage.html', 
                    {"user":user, 
                    "blogs": blogs, 
                    "events": events, 
                    "bands": bands, 
                    "places": places })
    except User.DoesNotExist:
        return render(request, '404.html')
  
  