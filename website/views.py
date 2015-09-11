from django.shortcuts import render

# Create your views here.

# Index page
def index(request):
    return render(request, "index.html")