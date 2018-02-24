from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import FormView
from django import http
from django.core import mail
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


def mail_send():
	connection = mail.get_connection()
	connection.open()
	email = mail.EmailMessage(
		'Subject here', 'Here is the message.', 'nightagenda.fun@gmail.com', ['mr.willentretenmert@gmail.com'],
		connection=connection,
	)
	email.send()
	connection.close()


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


class UserView(DetailView):
	model = User
	slug_url_kwarg = 'username'
	template_name = 'member/userpage.html'

	def get_object(self, queryset=None):
		user =  get_object_or_404(User, username=self.kwargs['username'])
		return user

	def get(self, *args, **kwargs):
		self.object = self.get_object()
		if self.object.is_superuser:
			return http.HttpResponseRedirect('/')
		return super(UserView, self).get(*args, **kwargs)
	
	def get_context_data(self, **kwargs):
		context = super(UserView, self).get_context_data(**kwargs)
		context['blogs'] = Blog.objects.filter(author=context['object'])
		context['events'] = Event.objects.filter(owner=context['object'])
		context['bands'] = Band.objects.filter(owner=context['object'])
		context['places'] = Place.objects.filter(owner=context['object'])
		return context