from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout  #inbuilt authenticate library
from django.contrib import messages  # this is used to show some sort of messages during login, logout etc....

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in....'))
            return redirect('home')
        else:
            messages.success(request, ('There was an error, please try again..'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, ('You have logged out... Thanks for stopping by......'))
    return redirect('home')
