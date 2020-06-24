from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return HttpResponse('Inside the Views INDEX function')
