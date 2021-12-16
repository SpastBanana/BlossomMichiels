from django.urls import path
from Sitemanager import views

urlpatterns = [
    path('', views.homeView, name="sitemanager"),
    path('home', views.homeView, name="sitemanager"),
    path('portPages', views.portPagesView, name="portPages"),
    path('portPages/<str:editPortPageName>', views.editPortPageView, name="editPortPages"),
    path('addPortPage', views.addPortPageView, name="addPortPage"),
]
