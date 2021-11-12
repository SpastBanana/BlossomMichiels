from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('sitemanager/', include('Sitemanager.urls')),
]
