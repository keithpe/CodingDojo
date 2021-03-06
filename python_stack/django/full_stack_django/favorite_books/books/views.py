from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login.models import *
from books.models import *


def show_books(request):

    # Get the user that is signed in, we want to check
    # which books the current user has liked/favorited
    this_user = User.objects.get(id=request.session['userid'])

    all_books = Book.objects.all()
    context = {'all_books': all_books,
               'this_user': this_user}

    return render(request, "show_books.html", context)


def show_book(request, id):

    this_book = Book.objects.get(id=id)
    this_user = User.objects.get(id=request.session['userid'])
    context = {'this_book': this_book,
               'this_user': this_user}

    return render(request, "show_book.html", context)


def create_book(request):

    # If this isn't a post request redirect to the main books route
    if request.method == 'GET':
        return redirect('/books')

    # Get a list of the errors form basic_validation
    # We'll use django messages to display error messages above the form
    errors = Book.objects.basic_validator(request.POST)

    if errors:
        # Loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

            # Save form info so we can display it back in the form when we get redirected.
            request.session['title'] = request.POST['title']
            request.session['description'] = request.POST['description']

        # redirect the user back to the form to fix the errors
        return redirect('/books/new')

    # Create new book object
    new_book = Book(title=request.POST['title'],
                    description=request.POST['description'], user_id=request.session['userid'])

    # Save new book object
    new_book.save()
    new_book.users_who_like.add(new_book.user_id)

    # Blank the title and description text in session, so they don't show up the next time we create a book.
    request.session['title'] = ''
    request.session['description'] = ''

    # Do we want to redirect to the edit page?
    # return redirect('/books/'+str(new_book.id)+'/edit')

    # Or do we just want to display the main page (add a favorite book/ All books page)
    return redirect('/books')


def add_to_favorites(request, id):

    # TODO: Need to add a try/except

    # Get the book object for this book id
    this_book = Book.objects.get(id=id)

    # Add this user to the favorites for this book.
    this_book.users_who_like.add(request.session['userid'])

    # Use HTTP_REFERER to return to the previous page (SHOW_BOOKS or SHOW_BOOK)
    return redirect(request.META['HTTP_REFERER'])


def remove_from_favorites(request, id):

    # TODO: Need to add a try/except
    # Get the book object for this book id
    this_book = Book.objects.get(id=id)

    # Add this user to the favorites for this book.
    this_book.users_who_like.remove(request.session['userid'])

    # return redirect('/books/'+id)
    return redirect(request.META['HTTP_REFERER'])


def edit_book(request, id):

    this_book = Book.objects.get(id=id)
    this_user = User.objects.get(id=request.session['userid'])
    context = {'this_book': this_book,
               'this_user': this_user}

    return render(request, "edit_book.html", context)


def update_book(request, id):

    # Get the book object
    this_book = Book.objects.get(id=id)

    # Update it with values from the form (title and description)
    this_book.title = request.POST['title']
    this_book.description = request.POST['description']

    # Now save it
    this_book.save()

    return redirect('/books/'+id)


def delete_book(request, id):
    # Delete the book

    this_book = Book.objects.get(id=id)
    this_book.delete()

    return redirect('/books')
