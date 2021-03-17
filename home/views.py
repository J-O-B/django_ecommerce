from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Homepage of website
    """
    return render(request, "home/index.html")