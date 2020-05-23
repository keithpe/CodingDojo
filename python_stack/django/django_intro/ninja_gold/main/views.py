from django.shortcuts import render, redirect, HttpResponse
import random


def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0

    return render(request, 'index.html')


def process_money(request):
    # Increment/Decrement depending on which button was pressed.
    print("request.POST", request.POST)
    print("request.POST['location']", request.POST['location'])

    gold_this_turn = 0
    if request.POST['location'] == 'farm':
        gold_this_turn = random.randint(10, 20)
    elif request.POST['location'] == 'cave':
        gold_this_turn = random.randint(5, 10)
    elif request.POST['location'] == 'house':
        gold_this_turn = random.randint(2, 5)
    elif request.POST['location'] == 'casino':
        gold_this_turn = random.randint(0, 50)

    request.session['gold'] += gold_this_turn

    return redirect('/')


def reset(request):
    if 'gold' in request.session:
        request.session['gold'] = 0
        return redirect('/')
