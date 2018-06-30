from django.conf.urls import url
from django.urls import path
from .views import index, users
app_name = "app"

urlpatterns = [
    path('', index, name="index"),
    path('users', users, name="user"),
]
