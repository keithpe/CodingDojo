from django.shortcuts import render, redirect, HttpResponse

from login.models import User
from books.models import *


def index(request):
    # return HttpResponse('Inside the BOOKS INDEX view')
    all_reviews = Review.objects.order_by('-created_at').all()
    all_books = Book.objects.all()

    context = {'all_reviews': all_reviews, 'all_books': all_books}

    return render(request, 'index.html', context)


def add_book(request):
    # return(HttpResponse('Inside ADD_BOOK view'))
    all_authors = Author.objects.all()
    context = {'all_authors': all_authors}

    return render(request, 'add_book.html', context)


def create_book(request):
    # Process/create new book in database and redirect to show book page

    # Use the User id to get the user object for the currently logged in user
    # We add it to the book and review records
    this_user = User.objects.get(id=request.session['userid'])

    # Get Author information
    # If author field in form is NOT empty pull author name from there...
    # ...otherwise use value from select_author field
    if request.POST['author'] != '':

        # Create the author bject...
        this_author = Author(name=request.POST['author'])

        # ...and save the author object
        this_author.save()

    else:
        # Use the author id in the select_author field to get the author object
        this_author = Author.objects.get(id=request.POST['select_author'])

    # Get Book Inforamtion
    this_book = Book(
        title=request.POST['title'], author=this_author, user=this_user)
    this_book.save()

    # Get Review Information
    this_review = Review(
        text=request.POST['review'], rating=request.POST['rating'], user=this_user, book=this_book)
    this_review.save()

    return redirect('/books/show_book/'+str(this_book.id))


def add_review(request, id):
    # Add a new review to the book with id

    # Get user and book objects so we can add them to the new review
    this_user = User.objects.get(id=request.session['userid'])
    this_book = Book.objects.get(id=id)

    # Create the review object from the form in request.POST
    this_review = Review(
        text=request.POST['review'], rating=request.POST['rating'], user=this_user, book=this_book)

    # Add the review to the database
    this_review.save()

    return redirect('/books/show_book/'+str(this_book.id))


def delete_review(request, id):
    # Delete the review with this id
    this_review = Review.objects.get(id=id)

    # Get the book object, so we can return to the same book page
    this_book = Book.objects.get(id=this_review.book.id)

    # Delete the review
    this_review.delete()

    # return redirect('/books')
    return redirect('/books/show_book/'+str(this_book.id))


def show_book(request, id):
    # Display existing book with render

    # Get the book object for the book id passed to this method
    this_book = Book.objects.get(id=id)

    # get all the reviews for the book id passed here
    this_book_reviews = Review.objects.filter(book=this_book)

    context = {'this_book': this_book, 'this_book_reviews': this_book_reviews}

    return render(request, 'show_book.html', context)


def show_user(request, id):
    # Display existing user and all the book they have reviewed

    # Get the user object
    this_user = User.objects.get(id=id)

    # Get all the reviews this user has posted
    all_reviews_for_this_user = Review.objects.filter(user=this_user)

    context = {'this_user': this_user,
               'all_reviews_for_this_user': all_reviews_for_this_user}

    return render(request, 'show_user.html', context)
