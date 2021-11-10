from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homeView, name='Home'),
    path('home', views.homeView, name='Home'),
    path('login', views.loginView, name="Login"),
    path('logout', views.logoutView, name="Logout"),
    path('profiel', views.profielView, name='Profiel'),
    path('about-me', views.aboutMeView, name='About-Me'),
    path('contact', views.contactView, name='Contact'),
    path('portfolio', views.portfolioView, name='Portfolio'),
    path('tarieven', views.tarievenView, name='Tarieven'),
    path('test', views.testView, name='Test'),
]
