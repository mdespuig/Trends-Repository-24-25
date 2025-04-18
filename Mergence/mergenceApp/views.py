from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def home(request):
 return render(request, "homepage.html")

def hotline(request):
 return render(request, "hotlines.html")

def login(request):
 if request.method == 'POST':
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()

    if not username or not password:
        messages.error(request, "All fields are required.")
        return render(request, 'login.html')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return redirect('home')
    else:
        messages.error(request, "Invalid username or password.")
        return render(request, 'login.html')

 return render(request, 'login.html')

def registration(request):
 return render(request, "registration.html")

def regForm(request):
 if request.method == 'POST':
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()
    confirm_password = request.POST.get('confirm-password', '').strip()

    if not username or not password or not confirm_password:
        messages.error(request, "All fields are required.")
        return render(request, 'registrationForm.html')

    if password != confirm_password:
        messages.error(request, "Passwords do not match.")
        return render(request, 'registrationForm.html')

    if User.objects.filter(username=username).exists():
        messages.error(request, "Username is already taken.")
        return render(request, 'registrationForm.html')

    user = User.objects.create(
        username=username,
        password=make_password(password)
    )
    return redirect('login')

 return render(request, 'registrationForm.html')