from django.shortcuts import render, redirect, HttpResponse


def index(request):
    # return HttpResponse("This is the root route for views.py")
    return render(request, "index.html")
