from django.shortcuts import render

# Create your views here.

# Index page
def index(request):
    return render(request, "index.html")


def projects(request):
    return render(request, "projects.html")


def press(request):
    return render(request, "press.html")


def images(request):
    return render(request, "images.html")


def contact(request):
    return render(request, "contact.html")