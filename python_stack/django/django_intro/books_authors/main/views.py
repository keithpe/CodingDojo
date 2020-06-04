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
        request.session['book_list'] += f"<p id='book_id'>{book.id}</p><p id='book_title'>{book.title}</p><p id='book_action'>VIEW\n</p>"

    return render(request, 'index.html')


def add_book(request):

    # Add the book to our database
    new_book = Book.objects.create(title=request.POST['title'])

    return redirect('/')


def authors(request):
    all_authors = Author.objects.all()
    print('all authors', all_authors)

    # Initial array to hold list of author information
    request.session['author_list'] = ''

    for author in all_authors:
        request.session['author_list'] += f"<p id='author_id'>{author.id}</p><p id='author_name'>{author.first_name+' '+ author.last_name}</p><p id='author_action'>VIEW\n</p>"

    return render(request, 'authors.html')


def add_author(request):
    # Add the author to our databas
    new_author = Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])

    return redirect('/authors')
