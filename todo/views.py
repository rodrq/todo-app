from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    return render(request, 'todo/home.html')


def registerPage(request):
    form = CreateUser(request.POST)
    if form.is_valid():
        form.save()
        return redirect('loginPage')
    context = {'form': form}
    return render(request, 'todo/registerPage.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'todo/loginPage.html')

    return render(request, 'todo/loginPage.html')
