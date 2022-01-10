from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
import datetime

from frontend.views import portPageView
from .models import portfolioPages, innerPortPageItems
from .forms import addPortPageForm
from django.core.files.storage import FileSystemStorage

def homeView(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    data = {
        'page': 'DataLectro-Sitemanager/home.html',
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def portPagesView(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    pages = portfolioPages.objects.all()
    data = {
        'page': 'DataLectro-Sitemanager/portPages.html',
        'pages': pages,
    }
    return render(request, 'DataLectro-Sitemanager/index.html', data)


def addPortPageView(request):
    if not request.user.is_authenticated:
        return redirect('/login')

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
    if not request.user.is_authenticated:
        return redirect('/login')
        
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
    if not request.user.is_authenticated:
        return redirect('/login')
        
    portPages = portfolioPages.objects.all()

    data = {
        'page': 'DataLectro-Sitemanager/editInnerPortPage.html',
        'pageName': str(editPortPageName),
        'format': innerPortPageItems.objects.all(),
    }

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def editPortPageFormatView(request, editPortPageName, formatName):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    if formatName == "whitespace":
        form = innerPortPageItems()
        form.portName = str(editPortPageName)
        form.rowFormat = "whitespace"
        form.text = "none"
        form.portimg1 = "none.jpg"
        form.portimg2 = "none.jpg"
        form.portimg3 = "none.jpg"
        form.save()
        return redirect('/sitemanager/portPages/' + str(editPortPageName))
    
    data = {
        'page': 'DataLectro-Sitemanager/editInnerPortPageFormat.html',
        'formatName': formatName,
        'portPage': editPortPageName,
        'content': innerPortPageItems.objects.all()
    }

    if formatName == "format1":
        if request.method == 'POST':
            form = innerPortPageItems()
            form.portName = str(editPortPageName)
            form.rowFormat = "form1"
            form.text = request.POST.get('text')
            form.portimg1 = request.FILES['img1']
            form.portimg2 = request.FILES['img2']
            form.save()

            return redirect('/sitemanager/portPages/' + str(editPortPageName))

    if formatName == "format2":
        if request.method == 'POST':
            form = innerPortPageItems()
            form.portName = str(editPortPageName)
            form.rowFormat = "form2"
            form.text = request.POST.get('text')
            form.portimg1 = request.FILES['img1']
            form.portimg2 = request.FILES['img2']
            form.save()

            return redirect('/sitemanager/portPages/' + str(editPortPageName))

    if formatName == "format3":
        if request.method == 'POST':
            form = innerPortPageItems()
            form.portName = str(editPortPageName)
            form.rowFormat = "form3"
            form.text = request.POST.get('text')
            form.portimg1 = request.FILES['img1']
            form.portimg2 = request.FILES['img2']
            form.save()

            return redirect('/sitemanager/portPages/' + str(editPortPageName))

    if formatName == "format4":
        if request.method == 'POST':
            form = innerPortPageItems()
            form.portName = str(editPortPageName)
            form.rowFormat = "form4"
            form.text = "none"
            form.portimg1 = request.FILES['img1']
            form.portimg2 = request.FILES['img2']
            form.portimg3 = request.FILES['img3']
            form.save()
            
            return redirect('/sitemanager/portPages/' + str(editPortPageName))

    return render(request, 'DataLectro-Sitemanager/index.html', data)


def deleteFormatView(request, portID, formatName):
    if not request.user.is_authenticated:
        return redirect('/login')

    data = {
        'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
    }
    
    if formatName == "form1":
        portPage = get_object_or_404(innerPortPageItems, pk=portID)
        portPage.portimg1.delete()
        portPage.portimg2.delete()
        deleted = portPage.rowFormat
        portPage.delete()
        
        data = {
            'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
            'deleted': deleted,
        }

    if formatName == "form2":
        portPage = get_object_or_404(innerPortPageItems, pk=portID)
        portPage.portimg1.delete()
        portPage.portimg2.delete()
        deleted = portPage.rowFormat
        portPage.delete()
        
        data = {
            'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
            'deleted': deleted,
        }

    if formatName == "form3":
        portPage = get_object_or_404(innerPortPageItems, pk=portID)
        portPage.portimg1.delete()
        portPage.portimg2.delete()
        deleted = portPage.rowFormat
        portPage.delete()
        
        data = {
            'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
            'deleted': deleted,
        }

    if formatName == "form4":
        portPage = get_object_or_404(innerPortPageItems, pk=portID)
        portPage.portimg1.delete()
        portPage.portimg2.delete()
        portPage.portimg3.delete()
        deleted = portPage.rowFormat
        portPage.delete()
        
        data = {
            'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
            'deleted': deleted,
        }

    if formatName == "whitespace":
        portPage = get_object_or_404(innerPortPageItems, pk=portID)
        deleted = portPage.rowFormat
        portPage.delete()

        data = {
            'page': 'DataLectro-Sitemanager/succesfullDeleted.html',
            'deleted': deleted,
        }

    return render(request, 'DataLectro-Sitemanager/index.html', data)