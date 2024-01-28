from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import User

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password'] 
        user = User(name=name, email=email, password=password)
        user.password = make_password(user.password)
        user.save()
        return redirect('homepage')  # Fix the redirect function here
    else:
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')





