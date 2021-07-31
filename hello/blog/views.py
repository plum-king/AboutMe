from django.shortcuts import redirect, render
from .models import BlogVisiter, Music, Hobby, Place, Pictures
from django.utils import timezone

# Create your views here.

def intro(request):
    return render(request, "intro.html")

def myhome(request):
    myhomes = BlogVisiter.objects.all()
    return render(request, "myhome.html", {'myhomes': myhomes})

def hobby(request):
    hob = Hobby.objects.all()
    return render(request, "hobby.html", {'hob': hob})

def music(request):
    return render(request, "music.html")

def pictures(request):
    return render(request, "pictures.html")

def place(request):
    return render(request, "place.html")

def guest(request):
    return render(request, "guest.html")

def create(request):
    new_blogvisit = BlogVisiter()
    new_blogvisit.name = request.POST['name']
    new_blogvisit.content = request.POST['body']
    new_blogvisit.date = timezone.now()
    new_blogvisit.save()
    return redirect('myhome')