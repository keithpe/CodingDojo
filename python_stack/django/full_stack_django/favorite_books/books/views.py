from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def show_books(request):
    # return HttpResponse('Inside show_books method')
    return render(request, "show_books.html")
