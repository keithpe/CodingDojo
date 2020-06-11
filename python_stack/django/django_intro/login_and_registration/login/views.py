from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, "login.html")


def registration(request):
    # Process the registration form
    request.session['process'] = request.POST['process']
    return redirect('login/success')


def login(request):
    # Process the login form
    request.session['process'] = request.POST['process']
    return redirect('login/success')


def logout(request):
    # Process the logout
    return redirect('/')


def success(request):
    return render(request, 'success.html')
