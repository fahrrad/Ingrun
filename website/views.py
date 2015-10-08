from django.shortcuts import render

# Create your views here.

# Index page
from website.models import TheaterPlay


def index(request):
    return render(request, "index.html")


def projects(request):
    theater_plays = TheaterPlay.objects.all()
    return render(request, "projects.html", {'theater_plays': theater_plays,
                                             'body_class': 'projects'})


def press(request):
    return render(request, "press.html", {'body_class': 'press'})


def images(request):
    return render(request, "images.html", {'body_class': 'images'})


def contact(request):
    return render(request, "contact.html", {'body_class': 'contact'})

