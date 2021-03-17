from django.shortcuts import render


def index(request):
    """
    Homepage of website
    """
    return render(request, "home/index.html")
