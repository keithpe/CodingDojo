from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'index.html')


def new(request):
    return render(request, 'new.html')


def create(request):
    # Add new book to database
    return redirect('/books/1')


def show(request, id):
    # Show current book and review
    return render(request, 'show.html')
