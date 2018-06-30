from django import forms
from django.contrib.auth.models import User
from .models import Victim
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username', 'password']

class VictimForm(forms.ModelForm):

    class Meta():
        model = Victim
        exclude = ['user', 'help_required', 'latitude', 'longitude']



class CustomUserLoginForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Username',
        }
    ))

    password = forms.CharField(label='Enter password', widget=forms.PasswordInput(
        attrs={
            'class': 'contact-input',
            'placeholder': 'Enter Password'
        }
    ))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        # if password1 and password2 and password1 != password2:
        #     raise ValidationError("Password don't match")

        return password
