from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('login', login_view, name="Login View"),
    path('register', register_view, name="Register View"),
    path('logout', logout_view, name="Logout View"),
   
]
