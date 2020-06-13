from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def show_books(request):
    # return HttpResponse('Inside show_books method')
    return render(request, "show_books.html")


def show_book(request, id):
    return render(request, "show_book.html")


def edit_book(request, id):
    return render(request, "edit_book.html")
