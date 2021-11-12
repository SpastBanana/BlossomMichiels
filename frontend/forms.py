from django import forms
from django.forms import ModelForm
from frontend.models import shootPayment, contactPage
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, PasswordInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=TextInput(attrs={'class': 'username','placeholder': 'Gebruikersnaam'}))
    password = forms.CharField(label='', widget=PasswordInput(attrs={'class': 'password','placeholder': 'Wachtwoord'}))

class shootPaymentForm(ModelForm):
    class Meta:
        model = shootPayment
        fields = '__all__'

class contactPageForm(ModelForm):
    class Meta:
        model = contactPage
        fields = '__all__'