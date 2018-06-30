from django.conf.urls import url
from django.urls import path
from .views import index, notifications, user, map, help, VictimSignup, VictimLogin, help_food, help_shelter, help_funding, needsHelp, notVictim
app_name = "app"

urlpatterns = [
    path('', index, name="index"),
    path('user', user, name="user"),
    path('notifications', notifications, name="notifications"),
    path('map', map, name="map"),
    path('help', help, name="help"),
    path('victimSignup', VictimSignup, name="victimSignup"),
    path('victimLogin', VictimLogin, name="victimLogin"),
    path('help-food', help_food, name="help_food"),
    path('help-shelter', help_shelter, name="help_shelter"),
    path('help-funding', help_funding, name="help_funding"),
    path('need-help', needsHelp, name="needsHelp"),
    path('notVictim', notVictim, name="notVictim"),
]
