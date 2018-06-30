from django.conf.urls import url
from django.urls import path
from .views import index, notifications, user, map
app_name = "app"

urlpatterns = [
    path('', index, name="index"),
    path('user', user, name="user"),
    path('notifications', notifications, name="notifications"),
]
