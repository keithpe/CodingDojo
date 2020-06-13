from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from books.models import *


def show_books(request):
    # return HttpResponse('Inside show_books method')
    all_books = Book.objects.all()
    context = {'all_books': all_books}

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

    print('id:', new_book.id)
    print('title:', new_book.title)
    print('description:', new_book.description)
    print('user_id:', new_book.user_id)

    # Do we want to redirect to the edit page?
    # return redirect('/books/'+str(new_book.id)+'/edit')

    # Or do we just want to display the main page (add a favorite book/ All books page)
    return redirect('/books')


def edit_book(request, id):
    return render(request, "edit_book.html")


def delete_book(request, id):
    # Delete the book
    return redirect('/books')
