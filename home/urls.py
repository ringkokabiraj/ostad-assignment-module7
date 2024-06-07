from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home, name="Homepage Rendering"),
    path('competitions/', competitions, name="competitions"),
    path('winners/', winners, name="winners"),
    path('cart/', cart, name="cart"),

    path('recent-tickets/', recent_tickets, name="recent_tickets"),
    path('account-details/', account_details, name="account_details"),

]
