from django.urls import path
from Sitemanager import views

urlpatterns = [
    path('', views.homeView, name="sitemanager"),
    path('home', views.homeView, name="sitemanager"),
    path('portPages', views.portPagesView, name="portPages"),
    path('portPages/delete/<int:portID>', views.deletePortPage, name="deletePortPages"),
    path('portPages/delete/<int:portID>/<str:formatName>', views.deleteFormatView, name="deletePortPages"),
    path('portPages/<str:editPortPageName>', views.editPortPageView, name="editPortPages"),
    path('portPages/<str:editPortPageName>/<str:formatName>', views.editPortPageFormatView, name="editPortPageFormats"),
    path('addPortPage', views.addPortPageView, name="addPortPage"),
]
