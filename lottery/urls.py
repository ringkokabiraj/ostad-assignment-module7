from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('lottery/<int:pk>/', view_lottery, name="Single Lottery View Page"),
    path('get_lottery_info/', GetLotteryDetails.as_view(), name=" Lottery Details API View"),
    path('get_category/<int:pk>/', single_lottery_view, name=" Category Wise Lottery Listing Page"),

]
