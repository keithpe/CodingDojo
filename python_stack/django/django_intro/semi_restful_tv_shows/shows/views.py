from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from shows.models import *
import datetime


def index(request):

    # Delete the request.sesssion when we're displaying all shows
    if 'title' in request.session:
        del request.session['title']

    all_shows = Show.objects.all()
    context = {'all_shows': all_shows}
    return render(request, 'index.html', context)


def add_show(request):

    # Set the session to blank
    if 'title' not in request.session:
        request.session['title'] = ''
        request.session['network'] = ''
        request.session['description'] = ''
        request.session['release_date'] = ''

    return render(request, 'new.html')


# Process new record from new.html (add_show)
def create_show(request):

    # Pass the post data to the validation method and save response in the errors variable
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # Loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        # Save form info so we can display it back in the form when we get redirected.
        request.session['title'] = request.POST['title']
        request.session['network'] = request.POST['network']
        request.session['description'] = request.POST['description']
        request.session['release_date'] = request.POST['release_date']

        # redirect the user back to the form to fix the errors
        return redirect('/new')

    # Code to create new show record
    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                                   release_date=request.POST['release_date'], description=request.POST['description'])

    # TODO: Move request.session assignments to a function?
    # Store in session
    request.session['title'] = new_show.title
    request.session['network'] = new_show.network
    request.session['release_date'] = new_show.release_date
    request.session['description'] = new_show.description
    request.session['updated_at'] = new_show.updated_at.strftime(
        "%B %d, %Y at %I:%M %p")

    return redirect('/shows/'+str(new_show.id))


def edit_show(request, id):
    this_show = Show.objects.get(id=id)

    # Store existing record data into request.session, but only the first time
    # once we're inside an editing session we'll pull the data from the form (request.POST).
    if 'title' not in request.session:
        request.session['title'] = this_show.title
        request.session['network'] = this_show.network
        request.session['release_date'] = this_show.release_date.strftime(
            '%Y-%m-%d')
        request.session['description'] = this_show.description

    # Convert to string so we can stuff it in the value of the edit screen
    this_show.release_date = this_show.release_date.strftime('%Y-%m-%d')

    context = {'this_show': this_show}
    return render(request, 'edit.html', context)


def update_show(request, id):

    # Pass the post data to the validation method and save response in the errors variable
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        # Save form info so we can display it back in the form when we get redirected.
        request.session['title'] = request.POST['title']
        request.session['network'] = request.POST['network']
        request.session['description'] = request.POST['description']
        request.session['release_date'] = request.POST['release_date']

        # redirect the user back to the form to fix the errors
        return redirect('/'+str(id)+'/edit')

    # Code to update posted data to record in database, then redirect
    this_show = Show.objects.get(id=id)

    this_show.title = request.POST['title']
    this_show.network = request.POST['network']
    this_show.release_date = request.POST['release_date']
    this_show.description = request.POST['description']

    # save() uses the 'auto_now=True', query filter update does not.
    this_show.save()

    # Clear requestion.session
    del request.session['title']

    return redirect('/shows/'+str(this_show.id))


def display_show(request, id):
    this_show = Show.objects.get(id=id)
    this_show.release_date = this_show.release_date.strftime('%B %d, %Y')
    context = {'this_show': this_show}
    return render(request, 'show_one.html', context)


def delete_show(request, id):
    Show.objects.filter(id=id).delete()
    return redirect('/shows')
