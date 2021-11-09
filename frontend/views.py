from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from .forms import SignUpForm, LoginForm
import datetime as datetime
import numpy as np

def homeView(request):
    template_name = 'home.html'
    return render(request, 'index.html', {'page': template_name})


def registerView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Login')
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'page': 'registration/register.html', 'form': form})


def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Home')
                else:
                    form = LoginForm
                    return render(request, 'index.html', {'page': 'registration/login.html', 'form': form, 'error': 'Account is not activated'})
            else:
                form = LoginForm
                return render(request, 'index.html', {'page': 'registration/login.html', 'form': form, 'error': 'Your username and password were incorrect.'})
        except:
            form = LoginForm
            return render(request, 'index.html', {'page': 'registration/login.html', 'form': form, 'error': 'Invalid Form'})

    else:
        form = LoginForm
        return render(request, 'index.html', {'page': 'registration/login.html', 'form': form, 'error': ''})

def logoutView(request):
    logout(request)
    return redirect('Home')


def profielView(request):
    if not request.user.is_anonymous:
        template_name = {'page': 'profiel.html'}
        return render(request, 'index.html', template_name)


def contactView(request):
    template_name = {'page': 'contact.html'}
    return render(request, 'index.html', template_name)


def aboutMeView(request):
    template_name = {'page': 'about-me.html'}
    return render(request, 'index.html', template_name)


def tarievenView(request):
    template_name = {'page': 'tarieven.html'}
    return render(request, 'index.html', template_name)


def portfolioView(request):
    template_name = {'page': 'portfolio.html'}
    return render(request, 'index.html', template_name)

