from django.shortcuts import render

# Create your views here.

# Index page
from website.models import TheaterPlay, PressCoverage, Movie, Exhibition


def index(request):
    return render(request, "index.html", {'body_class': 'index'})


def projects(request):
    theater_plays = TheaterPlay.objects.all()
    movies = Movie.objects.all()
    exhibitions = Exhibition.objects.all()
    return render(request, "projects.html", {'theater_plays': theater_plays,
                                             'movies': movies,
                                             'exhibitions': exhibitions,
                                             'body_class': 'projects'})


def press(request):
    press_coverages = PressCoverage.objects.all()
    return render(request, "press.html", {'press_coverages': press_coverages,
                                          'body_class': 'press'})


def images(request):
    return render(request, "images.html", {'body_class': 'images'})


def contact(request):
    return render(request, "contact.html", {'body_class': 'contact'})

