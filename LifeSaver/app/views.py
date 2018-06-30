from django.shortcuts import render
from .forms import VictimForm, UserForm
from django.contrib.auth.models import User
from .models import Victim
import pandas as pd
from .forms import CustomUserLoginForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

victim = False

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

    user = request.user
    context = {'user': user}
    return render(request, "app/landingPage.html", context)

def notifications(request):
    global victim
    return render(request, "app/notifications.html", {"victim":victim})

def user(request):
    global victim
    return render(request, "app/user.html", {"victim":victim})

def map(request):
    global victim
    return render(request, "app/map.html", {"victim":victim})

def help(request):
    global victim
    user = request.user
    victim = Victim.objects.get(user=user).help_required
    if user:
        context = {'user': user, "victim":victim}
    else:
        context = {"victim":victim}
    return render(request, "app/help.html", context)

def VictimSignup(request):
    global victim
    user = request.user
    context = {
        'signupForm': VictimForm,
        'userForm': UserForm,
        "victim":victim
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


def VictimLogin(request):
    global victim
    user = request.user
    print("Before request method")
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        print("Before form valid")

        username = request.POST['username']
        password = request.POST['password']
        print("Before authentication")
        user = authenticate(username=username, password=password)
        login(request, user)
        print("After authentication")
        return redirect('app:index')
    else:
        form = CustomUserLoginForm()

    context = {
        "form": form,
        "user": user,
        "victim":victim
    }
    return render(request, "app/victimLogin.html", context)

def help_food(request):
    user = request.user

    person = Victim.objects.get(user=user)

    if person.help_required == False:
        person.type_of_help = 'Food'
        person.save()

    return redirect('app:help')

def help_shelter(request):
    user = request.user

    person = Victim.objects.get(user=user)

    if person.help_required == False:
        person.type_of_help = 'Shelter'
        person.save()

    return redirect('app:help')

def help_funding(request):
    user = request.user

    person = Victim.objects.get(user=user)

    if person.help_required == False:
        person.type_of_help = 'Crowdfunding'
        person.save()

    return redirect('app:help')

def needsHelp(request):
    global victim
    user = request.user
    victim = Victim.objects.get(user=user)
    victim.help_required = True
    victim.save()
    victim = True
    context = {"victim": victim}
    return render(request, "app/need-help.html", context)

def notVictim(request):
    global victim
    user = request.user
    victim = Victim.objects.get(user=user)
    victim.help_required = False
    victim.save()
    victim = False

    context = {"victim": victim}
    return render(request, "app/help.html", context)
