from django.urls import path
from .views import login_view, redirect_login, register_view, home_view, logout_view

urlpatterns = [
    path('', redirect_login),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]