from django.shortcuts import render, HttpResponse
import datetime

from frontend.views import portPageView
from .models import portfolioPages
from .forms import addPortPageForm

def homeView(request):
    data = {
        'page': 'DataLectro-Sitemanager/home.html',
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def portPagesView(request):
    pages = portfolioPages.objects.all()
    data = {
        'page': 'DataLectro-Sitemanager/portPages.html',
        'pages': pages,
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def addPortPageView(request):
    addPortPage = addPortPageForm
    data = {
        'page': 'DataLectro-Sitemanager/addPortPage.html',
        'addForm': addPortPage,
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def editPortPageView(request, editPortPageName):
    portPages = portfolioPages.objects.all()
    data = {
        'page': 'DataLectro-Sitemanager/portPages.html',
        'portPages': portPages,
        'editPortPageName': editPortPageName,
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)