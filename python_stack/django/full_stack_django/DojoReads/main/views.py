from django.shortcuts import render, redirect, HttpResponse
from login.models import User
from main.models import Book, Review, Author


def index(request):
    all_reviews = Review.objects.all()
    all_books = Book.objects.all()
    context = {'all_reviews': all_reviews,
               'all_books': all_books}

    return render(request, 'index.html', context)


def new(request):

    # Get a list of all Authors. We'll display them for the user to choose from
    all_authors = Author.objects.all()
    context = {'all_authors': all_authors}
    return render(request, 'new.html', context)


def create(request):
    # Get the user object for the logged in user
    this_user = User.objects.get(id=request.session['userid'])

    # Add new book and review
    print(request.POST)

    if request.POST['author_name'] != '':
        # Check if that author name is already in the database
        # ...And if it is, then use the existing record, do not add a new author
        authors_found = Author.objects.filter(
            name=request.POST['author_name'].strip())
        if authors_found:
            this_author = authors_found[0]
        else:
            # Adding a new author
            this_author = Author(name=request.POST['author_name'].strip())
            this_author.save()
            print('new_author.name', this_author.name)

    else:
        print('Using an author from select list')
        # get the user pulled from the select menu
        this_author = Author.objects.get(id=request.POST['author_list'])
        print('this_author', this_author.name, this_author.id)

    # Add the book
    new_book = Book(title=request.POST['title'],
                    author=this_author, user=this_user)
    new_book.save()

    # Add the review
    new_review = Review(
        text=request.POST['review'], rating=request.POST['rating'], book=new_book, user=this_user)
    new_review.save()

    return redirect('/books/'+str(new_book.id))


def show(request, id):
    # Show current book and review
    this_book = Book.objects.get(id=id)
    this_book_reviews = Review.objects.filter(book=this_book)
    context = {'this_book_reviews': this_book_reviews,
               'this_book': this_book}

    return render(request, 'show.html', context)


def create_review(request, id):
    print('inside create review method')
    print('id', id)

    # Get the user object of the person adding this review
    this_user = User.objects.get(id=request.session['userid'])

    # Get the book object of book this review is for
    this_book = Book.objects.get(id=id)

    # Create a review for this book (id)
    new_review = Review(
        text=request.POST['review'], rating=request.POST['rating'], user=this_user, book=this_book)
    new_review.save()

    return redirect('/books/'+str(this_book.id))
