from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.


class LoginOrRegisterView(LoginView):
    template_name = 'registration/login.html'
