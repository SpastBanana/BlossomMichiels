from django.urls import path
from Sitemanager import views

urlpatterns = [
    path('', views.homeView, name="filemanager"),
    path('home/', views.homeView, name="filemanager"),
]
