from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from django.contrib import messages


def index(request):
    return render(request, "login.html")


def registration(request):
    # Process the registration form

    print("inside the registration method")

    request.session.flush()
    request.session['process'] = request.POST['process']

    print("About to run validator")
    errors = User.objects.basic_validator(request.POST)
    print("Finished running validator")

    print("About to check for errors")
    if errors:
        # Loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

            print('error:', value)

            # Save form info so we can display it back in the form when we get redirected.
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']
            request.session['email'] = request.POST['email']
            request.session['password'] = request.POST['password']

        # redirect the user back to the form to fix the errors
        return redirect('/')

        # Reset the request.session values
        request.session['first_name'] = ""
        request.session['last_name'] = ""
        request.session['email'] = ""
        request.session['password'] = ""

    return redirect('login/success')


def login(request):
    # Process the login form
    request.session.flush()
    request.session['process'] = request.POST['process']
    return redirect('login/success')


def logout(request):
    # Process the logout
    request.session.flush()
    return redirect('/')


def success(request):
    return render(request, 'success.html')
