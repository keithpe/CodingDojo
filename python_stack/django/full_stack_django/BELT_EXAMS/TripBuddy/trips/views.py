from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login.models import User
from trips.models import Trip


def index(request):

    # Get the user object for the currently logged in user
    this_user = User.objects.get(id=request.session['userid'])

    # Get a list of trips created by the currently logged in user
    this_users_trips = this_user.trips_created.all()

    # Get a list of trips the currently logged in user has joined
    this_users_trips_joined = this_user.trips_joined.all()

    # Get a list of trips created by anyone OTHER than the current user.
    # other_users_trips = Trip.objects.all()
    other_users_trips = Trip.objects.filter().exclude(created_by=this_user)

    context = {'this_users_trips': this_users_trips,
               'this_users_trips_joined': this_users_trips_joined,
               'other_users_trips': other_users_trips}

    return render(request, 'index.html', context)


def new(request):
    # Display form for user to enter new trip information
    if 'destination' not in request.session or request.session['destination'] != '':
        request.session['destination'] = ''
        request.session['plan'] = ''
        request.session['start_date'] = ''
        request.session['end_date'] = ''

    return render(request, 'new.html')


def create(request):
    # Create the new trip object and save it to the database

    # Run validation
    errors = Trip.objects.basic_validator(request.POST)

    if errors:
        # Loop through each key-value pair and make a flash messge
        for key, value in errors.items():
            messages.error(request, value)

        # Save form info so we can display it back in the form when we get redirected
        request.session['destination'] = request.POST['destination']
        request.session['plan'] = request.POST['plan']
        request.session['start_date'] = request.POST['start_date']
        request.session['end_date'] = request.POST['end_date']

        # redirect the user back to the form to fix the errors
        return redirect('/trips/new')

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

    # get a trip object for this trip
    this_trip = Trip.objects.get(id=id)

    # Stuff it into context so we can use it in the edit form
    context = {'this_trip': this_trip}

    # Get the record to edit push it to the form with context
    return render(request, 'edit.html', context)


def update(request, id):
    # Update the trip object

    print('request.POST', request.POST)

    # Get the original trip object
    this_trip = Trip.objects.get(id=id)

    # Run validation
    errors = Trip.objects.basic_validator(request.POST)

    if errors:
        # Loop through each key-value pair and make a flash messge
        for key, value in errors.items():
            messages.error(request, value)

        # Save form info so we can display it back in the form when we get redirected
        request.session['destination'] = request.POST['destination']
        request.session['plan'] = request.POST['plan']
        request.session['start_date'] = request.POST['start_date']
        request.session['end_date'] = request.POST['end_date']

        # redirect the user back to the form to fix the errors
        return redirect('/trips/'+str(this_trip.id)+'/edit')

    # Update this_trip
    this_trip.destination = request.POST['destination']
    this_trip.plan = request.POST['plan']
    this_trip.start_date = request.POST['start_date']
    this_trip.end_date = request.POST['end_date']

    # Now save it
    this_trip.save()

    return redirect('/trips')


def show(request, id):
    # Show an existing trip

    # Get the trip object for the trip id
    this_trip = Trip.objects.get(id=id)

    # Get a list of the people who have joined the trip
    this_trip_joiners = this_trip.joiners.all()

    # Stuff it into context, so we can use it in show.html
    context = {'this_trip': this_trip, 'this_trip_joiners': this_trip_joiners}

    # Get the record to edit push it to the form with context
    return render(request, 'show.html', context)


def delete(request, id):
    # Delete a Trip

    # Get the trip object for the trip id
    this_trip = Trip.objects.get(id=id)

    # Delete this trip object
    this_trip.delete()

    return redirect('/trips')


def join(request, id):
    # Join the current user to this trip

    # Get Trip object for this current trip id
    this_trip = Trip.objects.get(id=id)

    # Get the User object for the currently logged in user
    this_user = User.objects.get(id=request.session['userid'])

    # Add it to the list of users/joiners in this trip
    this_trip.joiners.add(this_user)

    return redirect('/trips')


def cancel(request, id):
    # Cancel this trip for the currently logged in user

    # Get the trip object for this trip
    this_trip = Trip.objects.get(id=id)

    # Get the user object for this currently logged in user
    this_user = User.objects.get(id=request.session['userid'])

    this_trip.joiners.remove(this_user)

    return redirect('/trips')
