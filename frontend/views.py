import os

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from BlossomSite import settings
from .forms import LoginForm
from .forms import shootPaymentForm
from .models import shootPayment, contactPage
from django.core.files.storage import FileSystemStorage

def makeMailClient(mail):
    MSG = '''
    Bedankt voor het invullen van ons contact formulier! Hierbij is bevestigd dat
    wij uw mail ontvangen hebben. Wij zullen zo spoedig mogelijk contact met
    u opnemen!

    Vriendelijke groet,
    Blossom Michiels
    '''
    send_mail('Bevestiging WebForm BlossomMichiels', MSG, 'noreply@blossommichiels.nl', [mail],
              fail_silently=False, auth_user='noreply@blossommichiels.nl', auth_password='P1cture.20')


def makeMailDataLectro(name, mail, sub, msg):
    data = {'name': name, 'mail': mail, 'sub': sub, 'msg': msg}
    MSG = '''
Webmail van:        {}
Mail adres:             {}

Message: 
{}
    '''.format(data['name'], data['mail'], data['msg'])

    send_mail(sub, MSG, 'webmail@blossommichiels.nl', ['info@blossommichiels.nl'],
              fail_silently=False, auth_user='webmail@blossommichiels.nl', auth_password='P1cture.20')



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
    if request.method == 'POST' and 'submitMail' in request.POST:
        name = request.POST.get('name')
        mail = request.POST.get('email')
        sub = "MSG from web form"
        msg = request.POST.get('message')
        makeMailClient(mail)
        makeMailDataLectro(name, mail, sub, msg)
        contact = contactPage.objects.all()
        data = {'page': 'contact.html', 'contactText': contact, 'name': name, 'mail': mail, 'sub': sub, 'msg': msg}
        return render(request, 'index.html', data)
    else:
        contact = contactPage.objects.all()
        data = {'page': 'contact.html', 'contactText': contact}
        return render(request, 'index.html', data)


def aboutMeView(request):
    template_name = {'page': 'about-me.html'}
    return render(request, 'index.html', template_name)


def tarievenView(request):
    tarieven = shootPayment.objects.all()
    template_name = {'page': 'tarieven.html', 'tarieven': tarieven}
    return render(request, 'index.html', template_name)


def portfolioView(request):
    template_name = {'page': 'portfolio.html'}
    return render(request, 'index.html', template_name)

def testView(request):
    template_name = {'page': 'test.html'}
    return render(request, 'index.html', template_name)

def uploadView(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'index.html', {'file_url': file_url, 'page': 'uploadTest.html'})
    return render(request, 'index.html', {'page': 'uploadTest.html'})
