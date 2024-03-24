from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, authenticate, logout


# Create your views here.

def index_page(request):
    return render(request, 'main/index/index.html')


def login_page(request):
    if request.method == "GET":
        return render(request, 'main/auth/login_page.html', context={
            'login_form': AuthenticationForm()
        })
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/auth/login_page.html', context={
            'login_form': AuthenticationForm(),
            'error': 'Неверное имя пользователя или пароль' 
        })
        else:
            login(request, user)
            return redirect('index_page')


def logout_user(requets):
    if requets.method == "POST":
        logout(requets)
        return redirect('index_page')
