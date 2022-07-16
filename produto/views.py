from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(requests):
    return render(requests, 'home.html', {'nome': 'Lucas'})