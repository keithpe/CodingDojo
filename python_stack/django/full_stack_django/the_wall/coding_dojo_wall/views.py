from django.shortcuts import render, redirect, HttpResponse


def index(request):
    # return HttpResponse('Inside the CODING DOJO WALL index method')
    return render(request, 'index.html')
