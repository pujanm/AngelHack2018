from django.shortcuts import render
from .forms import VictimForm, UserForm
from django.contrib.auth.models import User
from .models import Victim
import pandas as pd

# Create your views here.

def index(request):
    # df = pd.read_csv("hospital_directory.csv", low_memory=False)
    # mumbai_hosp = df.loc[(df["District"] == "Mumbai") & (pd.notnull(df["Location_Coordinates"]) & (df["Location_Coordinates"] != "Error"))]
    #
    # csv_df = mumbai_hosp.loc[:, ["Location_Coordinates", "Location", "Hospital_Name", "State", "District"]]
    # for i in range(len(csv_df)):
    #     if type(df.loc[i, "Location_Coordinates"]) == str and df.loc[i, "Location_Coordinates"] != "Error":
    #
    #         lat = df.loc[i, "Location_Coordinates"].split(", ")[0]
    #         long = df.loc[i, "Location_Coordinates"].split(", ")[1]
    #         name = df.loc[i, "Hospital_Name"]
    #
    #         hospital = Hospitals.objects.create(name=name, latitude=lat, longitude=long)

    return render(request, "app/dashboard.html", {})

def notifications(request):
    return render(request, "app/notifications.html", {})

def user(request):
    return render(request, "app/user.html", {})

def map(request):
    return render(request, "app/map.html", {"hi":"bye"})

def help(request):
    return render(request, "app/help.html", {})

def VictimSignup(request):
    context = {
        'signupForm': VictimForm,
        'userForm': UserForm,
    }
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        victim_form = VictimForm(request.POST, request.FILES)
        if user_form.is_valid() and victim_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            victim = victim_form.save(commit=False)
            victim.user = user
            victim.photo = request.FILES['photo']
            victim.latitude = request.POST.get("lat");
            victim.longitude = request.POST.get("lng");
            victim.save()
            return render(request, "app/victimSignup.html", context)
        return render(request, "app/victimSignup.html", context)
            # login(request, authenticate(username=username, password=raw_password))
    return render(request, "app/victimSignup.html", context)
