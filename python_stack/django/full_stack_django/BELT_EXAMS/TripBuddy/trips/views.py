from django.shortcuts import render, redirect, HttpResponse


def index(request):
    # return HttpResponse('Inside the trips index def')
    return render(request, 'index.html')


def new(request):
    # Display form for user to enter new trip information

    return render(request, 'new.html')
