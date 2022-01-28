from django.urls import path
from .views import follow, followers_count, register, profile, home

urlpatterns = [
    path('home/', home, name='home'),
    path('follow/', follow, name='follow'),
    path('followers_count/', followers_count, name='followers_count'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]