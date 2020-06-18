from django.shortcuts import render, redirect, HttpResponse


def index(request):
    # return HttpResponse('Inside the trips index def')
    return render(request, 'index.html')
