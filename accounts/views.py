from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as dj_login, logout
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST['username']
        # password = request.POST['password']

        # user = authenticate(request, username=username,password=password)
        user = authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password invalid')

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return redirect('register')

        # Check User
        user = User.objects.filter(username=username).exists()
        if user:
            messages.error(request,'User already exists')
            return redirect('register')

        # Check Email
        user = User.objects.filter(email=email).exists()
        if user:
            messages.error(request,'Email already exists')
            return redirect('register')

        user = User.objects.create_user(username=username,
                password=password, email=email, first_name=first_name,
                last_name=last_name)
        # # Login after Register
        # auth.login(request, user)
        # messages.success(request, 'You are logged in')
        # return redirect('index')
        user.save();
        messages.success(request, 'You are registered')
        return redirect('dashboard')
    else:
        return render(request,'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are logged out')
        return redirect('login')

def dashboard(request):
    return render(request,'accounts/dashboard.html')
