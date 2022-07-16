from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('categoria/<int:id>', views.categorias, name="categoria"),
    path('produto/<int:id>', views.produtos, name="produto")
]