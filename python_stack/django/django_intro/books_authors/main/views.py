from django.shortcuts import render, redirect, HttpResponse
from main.models import *


def index(request):
    print("inside index() of views.py")

    # Retrieve all books in database
    all_books = Book.objects.all()
    print('all_books', all_books)

    # Initial array to hold list of book information
    request.session['book_list'] = ''

    for book in all_books:
        print('book.title', book.id, book.title)
        request.session['book_list'] += f"<p id='book_id'>{book.id}</p><p id='book_title'>{book.title}</p><p id='book_action'>VIEW\n</p>"

    return render(request, 'index.html')


def add_book(request):
    return HttpResponse("Inside add_book")
