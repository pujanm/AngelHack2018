from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app/dashboard.html", {})

def notifications(request):
    return render(request, "app/notifications.html", {})

def user(request):
    return render(request, "app/user.html", {})

def map(request):
    return render(request, "app/map.html", {})

def help(request):
    return render(request, "app/help.html", {})
