"""Defines URL patterns for users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = "users"
urlpatterns = [
    # Login page
    path("", views.LoginView.as_view(), name="login"),

    # Logout page
    path("logout/", views.logout_view, name="logout"),
]