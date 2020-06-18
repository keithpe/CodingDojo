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


def edit(request, id):
    # Edit (display form) an existing trip
    print("Inside the EDIT def")

    # Get the record to edit push it to the form with context
    return render(request, 'edit.html')


def update(request):
    # Update the trip object
    print("Inside the UPDATE def")

    # Create a TRIP object withi values from the form and then save the object

    return redirect('/trips')
