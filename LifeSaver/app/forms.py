from django import forms
from django.contrib.auth.models import User
from .models import Victim

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username', 'password']

class VictimForm(forms.ModelForm):

    class Meta():
        model = Victim
        exclude = ['user', 'help_required', 'latitude', 'longitude']
