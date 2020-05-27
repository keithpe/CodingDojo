from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('placeholder to display a list of all of the users')


def register(reqeust):
    return HttpResponse('placeholder for users to create a new user record')


def login(request):
    return HttpResponse('placeholder for users to login')


def new(request):
    return redirect('/users/register')
