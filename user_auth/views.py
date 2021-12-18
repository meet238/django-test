# Create your views here.
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView, RedirectView

from user_auth.forms import RegisterForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'
    success_url = 'index'

    def form_valid(self, form):
        user = auth.authenticate(**form.cleaned_data)
        if user:
            auth.login(self.request, user)
            return redirect('index')
        return redirect('login')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = 'login'


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
