from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    if not 'attempt' in request.session:
        return redirect('/random_word')

    return render(request, 'index.html')


def random_word(request):
    if request.method == 'POST':

        if 'attempt' in request.session:
            request.session['attempt'] += 1
        else:
            request.session['attempt'] = 1

    request.session['word'] = get_random_string(14).upper()
    return redirect('/')


def reset(request):
    request.session['attempt'] = 1
    return redirect('/random_word')
