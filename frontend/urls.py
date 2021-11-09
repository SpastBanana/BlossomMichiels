from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homeView, name='Home'),
    path('home', views.homeView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('register', views.registerView, name="Register"),
    path('profiel', views.profielView, name='Profiel'),

]
