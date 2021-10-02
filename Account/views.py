from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Login Failed !")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, "Password confirmation does not match")
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['email'],
                                            request.POST['password1'])
            user.save()
            messages.success(request, "Sign Up Successfully")
            return redirect('login')
    return render(request, 'register.html')


def log_out(request):
    logout(request)
    return redirect('home')
