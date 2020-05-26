from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('placeholder to display a list of all blogs')


def new(request):
    return HttpResponse('placeholder to create a new blog')


def create(request):
    return redirect('/blogs')


def show(request, number):
    return HttpResponse(f'placeholder to display blog number: {number}')


def edit(request, number):
    return HttpResponse(f'placeholder to edit blog number: {number}')


def destroy(request, number):
    print(f'Destroying blog number: {number}')
    return redirect('/blogs')
