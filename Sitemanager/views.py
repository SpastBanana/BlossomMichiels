from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
import datetime

def homeView(request):
    data = {
        'page': 'DataLectro-Sitemanager/home.html'
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)