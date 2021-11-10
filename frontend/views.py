import os

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from BlossomSite import settings
from .forms import LoginForm
import datetime as datetime
import numpy as np

def homeView(request):
    homeSlidePath = settings.BASE_DIR / 'static/IMG/Home-Slide'
    imgList = os.listdir(homeSlidePath)
    data = {
        'page': 'home.html',
        'images': imgList,
        'imgCount': range(len(imgList)),
    }
    return render(request, 'index.html', data)


def loginView(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('filemanager')
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
    else:
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

def testView(request):
    template_name = {'page': 'test.html'}
    return render(request, 'index.html', template_name)

