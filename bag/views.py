from django.shortcuts import render


def view_bag(request):
    """
    A view of a users shopping bag
    """
    return render(request, "bag/bag.html")
