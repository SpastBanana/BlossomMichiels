from django import forms
from django.forms import ModelForm
from .models import portfolioPages

class addPortPageForm(ModelForm):
    class Meta:
        model = portfolioPages
        fields = '__all__'