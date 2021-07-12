from django.shortcuts import render
from .models import Blog
# Create your views here.

def intro(request):
    return render(request, "intro.html")

def myhome(request):
    return render(request, "myhome.html")

def hobby(request):
    return render(request, "hobby.html")

def music(request):
    return render(request, "music.html")

def pictures(request):
    return render(request, "pictures.html")

def place(request):
    return render(request, "place.html")