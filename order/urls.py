from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', checkout_view, name="CheckOut View Page"),

]
