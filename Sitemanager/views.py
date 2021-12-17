from django.shortcuts import get_object_or_404, render, HttpResponse
import datetime

from frontend.views import portPageView
from .models import portfolioPages
from .forms import addPortPageForm
from django.core.files.storage import FileSystemStorage

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

    data = {
        'page': 'DataLectro-Sitemanager/addPortPage.html',
    }

    if request.method == 'POST':
        form = addPortPageForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()

        # form = portfolioPages()
        # form.portName = request.POST.get('portName')
        # form.img1 = request.POST.get('img1')
        # file1 = request.FILES['img1']
        # form.img2 = request.POST.get('img2')
        # file2 = request.FILES['img2']
        # form.img3 = request.POST.get('img3')
        # file3 = request.FILES['img3']

        # fs = FileSystemStorage()
        # fs.save(file1.name, file1)
        # fs.save(file2.name, file2)
        # fs.save(file3.name, file3)
        # form.save()

        return render(request, 'DataLectro-Sitemanager/index.html', data)

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def deletePortPage(request, portID):
    portPage = get_object_or_404(portfolioPages, pk=portID)
    portPage.img1.delete()
    portPage.img2.delete()
    portPage.img3.delete()
    deleted = portPage.portName
    portPage.delete()

    data = {
        'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
        'deleted': deleted,
    }

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def editPortPageView(request, editPortPageName):
    portPages = portfolioPages.objects.all()

    data = {
        'page': 'DataLectro-Sitemanager/portPages.html',
        'pages': portPages,
    }

    
    
    return render(request, 'DataLectro-Sitemanager/index.html', data)