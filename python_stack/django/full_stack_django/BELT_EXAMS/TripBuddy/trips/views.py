from django.shortcuts import render, redirect, HttpResponse


def index(request):
    # return HttpResponse('Inside the trips index def')
    print("Inside the INDEX def")

    return render(request, 'index.html')


def new(request):
    # Display form for user to enter new trip information
    print("Inside the NEW def")

    return render(request, 'new.html')


def create(request):
    # Create the new trip object and save it to the database
    print("Inside the CREATE def")
    return redirect('/trips')
