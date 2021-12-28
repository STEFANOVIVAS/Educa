from django.urls import path
from .views import LoginOrRegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', LoginOrRegisterView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
