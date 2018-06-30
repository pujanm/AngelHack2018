from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "app/landingPage.html", {})

def notifications(request):
    return render(request, "app/notifications.html", {})

def user(request):
    return render(request, "app/user.html", {})

def map(request):
    return render(request, "app/map.html", {})

def help(request):
    initial = True
    needsHelp = False
    wantsToHelp = False
    return render(request, "app/help.html", {'initial':initial,
                                             'needsHelp': needsHelp,
                                              'wantsToHelp':wantsToHelp})
