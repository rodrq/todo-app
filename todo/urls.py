from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='registerPage'),
    path('logout/', views.logoutPage, name='logout'),
    path('login/', views.loginPage, name='loginPage'),


]
