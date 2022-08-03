from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, f"Bienvenue {user.username}")
            return redirect('hangar:index')
        else:
            messages.error(request, 'Username or password not matches !')
            return redirect('account:login')
    return render(request, 'account/login.html')

def user_logout(request):
    logout(request)
    return redirect('hangar:index')