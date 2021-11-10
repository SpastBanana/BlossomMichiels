import shutil

from django.shortcuts import render
from BlossomSite import settings

def uploadView(request):
    data = {
        'page': 'DataLectro-Filemanager/upload.html',
    }
    if request.method == 'POST':
        uploadedFile = request.FILES['document']
        uploadDir = settings.BASE_DIR / 'static/test'
        shutil.move(uploadedFile, uploadDir)
    return render(request, 'DataLectro-Filemanager/index.html', data)