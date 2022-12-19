from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    # path('blogs', views.blogs, name='blogs'),
    # path('events', views.events, name='event'),
    # path('register', views.events, name='register'),
    # path('login', views.login, name='login'),
]
