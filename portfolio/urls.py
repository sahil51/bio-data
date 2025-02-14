from django.urls import path
from django.contrib import admin
from portfolio import views
urlpatterns = [
    path('',views.home)
]

