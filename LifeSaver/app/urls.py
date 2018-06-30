from django.conf.urls import url
from django.urls import path
from .views import index, notifications, user, map, help, VictimSignup, VictimLogin
app_name = "app"

urlpatterns = [
    path('', index, name="index"),
    path('user', user, name="user"),
    path('notifications', notifications, name="notifications"),
    path('map', map, name="map"),
    path('help', help, name="help"),
    path('victimSignup', VictimSignup, name="victimSignup"),
    path('login', VictimLogin, name="victimLogin"),
]
