from django.shortcuts import render, redirect, HttpResponse
from login.models import User
from trips.models import Trip


def index(request):
    print("Inside the INDEX def")

    # Get the user object for the currently logged in user
    this_user = User.objects.get(id=request.session['userid'])

    # Get a list of trips created by the currently logged in user
    this_users_trips = this_user.trips_created.all()

    # Get a list of trips created by anyone OTHER than the current user.
    # other_users_trips = Trip.objects.all()
    other_users_trips = Trip.objects.filter().exclude(created_by=this_user)

    context = {'this_users_trips': this_users_trips,
               'other_users_trips': other_users_trips}

    return render(request, 'index.html', context)


def new(request):
    # Display form for user to enter new trip information
    return render(request, 'new.html')


def create(request):
    # Create the new trip object and save it to the database
    print("Inside the CREATE def")

    # Get the object of the user who is creating this trip
    this_user = User.objects.get(id=request.session['userid'])

    # Create a trip object form new.html form values
    this_trip = Trip(destination=request.POST['destination'], plan=request.POST['plan'],
                     start_date=request.POST['start_date'], end_date=request.POST['end_date'], created_by=this_user)

    # Save the trip object
    this_trip.save()

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


def show(request, id):
    # Show an existing trip
    print("Inside the SHOW def")

    # Get the record to edit push it to the form with context
    return render(request, 'show.html')
