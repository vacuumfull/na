from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


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
        login(self.request, user)
        return super().form_valid(form)
