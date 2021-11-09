from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=TextInput(attrs={'class': 'username','placeholder': 'Gebruikersnaam'}))
    password = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'password','placeholder': 'Wachtwoord'}))