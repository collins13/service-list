from django.urls import path
from . import views


urlpatterns = [
    path('/signup', views.signup, name='signup'),
    path('/login', views.login_view, name='login'),
    path('/profile', views.profile, name='profile'),
    path('/verified', views.verified, name='verified'),
    path('/email', views.email, name='email'),
    path('/logout', views.logout_view, name='logout'),
]
