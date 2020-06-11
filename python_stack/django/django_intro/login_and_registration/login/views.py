from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from django.contrib import messages


def index(request):
    return render(request, "login.html")


def registration(request):
    # Process the registration form

    request.session['process'] = request.POST['process']

    errors = User.objects.basic_validator(request.POST)

    if errors:
        # Loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

            # Save form info so we can display it back in the form when we get redirected.
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']
            request.session['email'] = request.POST['email']
            request.session['password'] = request.POST['password']

        # redirect the user back to the form to fix the errors
        return redirect('/')

    # Save the first name so we can display it on the success page.
    request.session['first_name'] = request.POST['first_name']

    # Set a session variable to indicate that we've successfully logged in. (access to success page will require it.)
    request.session['status'] = 'success'

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
    # Check if the status key exists in the request.session dictionary.
    # If it doesn't or if it's not set to 'success' than we'll redirect to the login page
    # We don't want someone to be able to access this page from their browser UNLESS they successfully login to the server
    if 'status' in request.session:
        if request.session['status'] != 'success':
            request.session.flush()
            return redirect('/')
    else:
        return redirect('/')

    return render(request, 'success.html')
