from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from authentication.forms import *


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('customers')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('logout')


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)

# Create your views here.
