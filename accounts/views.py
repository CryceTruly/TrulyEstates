from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            # check usernemailame
            if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return redirect('register')
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            # auth.login(user, request)
            # messages.success(request, 'You are now registered and logged in')
            # return redirect('')

            user.save()
            messages.success(
                request, 'You are now registered and can logged in')
            return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        messages.add_message(request, messages.INFO, 'Hello world.')
        return redirect('login')
    return render(request, "accounts/login.html")


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")
