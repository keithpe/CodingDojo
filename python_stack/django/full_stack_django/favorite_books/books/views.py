from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from books.models import *


def show_books(request):
    # return HttpResponse('Inside show_books method')

    # Get the user that is signed in, we want to check
    # which books the current user has liked/favorited
    this_user = User.objects.get(id=request.session['userid'])
    print('this_user.first_name=', this_user.first_name)

    all_books = Book.objects.all()
    context = {'all_books': all_books,
               'this_user': this_user}

    return render(request, "show_books.html", context)


def show_book(request, id):
    return render(request, "show_book.html")


def create_book(request):
    print("**** Inside create_book ****")

    # Create new book object
    new_book = Book(title=request.POST['title'],
                    description=request.POST['description'], user_id=request.session['userid'])

    # Save new book object
    new_book.save()
    new_book.users_who_like.add(new_book.user_id)

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

    return redirect('/books')


def edit_book(request, id):
    print("inside edit_book")
    this_book = Book.objects.get(id=id)
    context = {'this_book': this_book}

    return render(request, "edit_book.html", context)


def delete_book(request, id):
    # Delete the book
    return redirect('/books')
