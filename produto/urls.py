from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.home, name="home")
]