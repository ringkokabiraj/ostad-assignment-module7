from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('lottery/<int:pk>/', view_lottery, name="Single Lottery View Page"),

]
