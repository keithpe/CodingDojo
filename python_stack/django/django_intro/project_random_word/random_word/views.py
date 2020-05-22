from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    return redirect('/random_word')


def random_word(request):

    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1

    request.session['word'] = get_random_string(14).upper()
    return render(request, 'index.html')


def reset(request):
    request.session['attempt'] = 0
    return redirect('/random_word')
