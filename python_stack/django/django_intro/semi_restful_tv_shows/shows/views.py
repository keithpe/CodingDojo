from django.shortcuts import render, redirect, HttpResponse
from shows.models import *
import datetime


def index(request):
    all_shows = Show.objects.all()
    context = {'all_shows': all_shows}
    return render(request, 'index.html', context)

# Display add form


def add_show(request):
    return render(request, 'new.html')


# Process new record from new.html (add_show)
def create_show(request):

    # Code to create new show record
    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                                   release_date=request.POST['release_date'], description=request.POST['description'])

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

    # Convert to string so we can stuff it in the value of the edit screen
    this_show.release_date = this_show.release_date.strftime('%Y-%m-%d')

    context = {'this_show': this_show}
    return render(request, 'edit.html', context)


def update_show(request, id):
    # Code to update posted data to record in database, then redirect
    this_show = Show.objects.get(id=id)

    # Update the existing record
    Show.objects.filter(id=id).update(title=request.POST['title'], network=request.POST['network'],
                                      release_date=request.POST['release_date'], description=request.POST['description'])

    return redirect('/shows/'+str(this_show.id))


def display_show(request, id):
    this_show = Show.objects.get(id=id)
    context = {'this_show': this_show}
    return render(request, 'show_one.html', context)


def delete_show(request, id):
    Show.objects.filter(id=id).delete()
    return redirect('/shows')
