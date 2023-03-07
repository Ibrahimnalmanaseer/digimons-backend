from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', DigimonListView.as_view(),name="digimon_list"),
     path('<int:pk>', DigimonDetailView.as_view(),name="digimon_detail"),
]
