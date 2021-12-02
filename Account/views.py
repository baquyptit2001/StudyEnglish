from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import check_password
from .models import Profile


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
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            if User.objects.filter(email=request.POST['email']).exists():
                messages.error(request, "Email already exists")
                return redirect('register')
            user = User.objects.create_user(request.POST['username'], request.POST['email'],
                                            request.POST['password1'])
            user.save()
            p = Profile()
            p.name = user.username
            p.image = 'avt.jpg'
            p.save()
            messages.success(request, "Sign Up Successfully")
            return redirect('login')
    return render(request, 'register.html')


@login_required()
def log_out(request):
    logout(request)
    return redirect('home')


@login_required()
def change_password(request):
    a = request.user.password
    if request.method == "POST":
        if request.POST['new_password1'] != request.POST['new_password2']:
            messages.error(request, "Confirm new password is incorrect")
        elif not check_password(request.POST['old_password'], a):
            messages.error(request, "Incorrect old password")
        else:
            u = User.objects.get(username=request.user.username)
            u.set_password(request.POST['new_password1'])
            u.save()
            messages.success(request, "Change password successfully")
            return redirect('login')
    return render(request, 'change_password.html')


@login_required()
def profile(request):
    p = Profile.objects.filter(name=request.user.username)
    if not p.all():
        p = Profile()
        p.name = request.user.username
        p.image = 'avt.jpg'
        p.save()
        return render(request, 'profile.html', {'p': p})
    p = Profile.objects.get(name=request.user.username)
    if request.method == "POST":
        p.first_name = request.POST['first_name']
        p.last_name = request.POST['last_name']
        p.email = request.POST['email']
        p.phone = request.POST['phone']
        p.country = request.POST['country']
        p.language = request.POST['language']
        if request.FILES.get('image', False):
            a = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(a.name, a)
            p.image = a
        p.save()
        return render(request, 'profile.html', {'p': p})
    return render(request, 'profile.html', {'p': p})
