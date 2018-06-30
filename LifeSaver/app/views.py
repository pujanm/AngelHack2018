from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app/dashboard.html", {})

def users(request):

    return render(request, "app/user.html", {})


def maps(request):

    return render(request, "app/maps.html", {})
