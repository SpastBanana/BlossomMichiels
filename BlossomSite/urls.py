from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('sitemanager/', include('Sitemanager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
