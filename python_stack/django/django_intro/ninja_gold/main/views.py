from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime


def index(request):

    # If the session info does not yet exist, then create them
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'activity_log' in request.session:
        request.session['activity_log'] = ""

    return render(request, 'index.html')


def process_money(request):
    # Increment/Decrement depending on which button was pressed.
    print("request.POST", request.POST)
    print("request.POST['location']", request.POST['location'])
    print("activity_log", request.session)

    # Determine which location button was pressed and determine
    # the amount (increased or decreased)
    gold_this_turn = 0
    if request.POST['location'] == 'farm':
        gold_this_turn = random.randint(10, 20)
    elif request.POST['location'] == 'cave':
        gold_this_turn = random.randint(5, 10)
    elif request.POST['location'] == 'house':
        gold_this_turn = random.randint(2, 5)
    elif request.POST['location'] == 'casino':
        gold_this_turn = random.randint(0, 50)

    # Determine if we're adding or removing gold from the gold stash
    if random.randint(0, 1) == 0:
        increase = False
    else:
        increase = True

    print("increase", increase)

    # Get date info for activity log.
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")

    # Update the total amount of gold and the activity log entry.
    if increase == True:
        request.session['gold'] += gold_this_turn
        request.session['activity_log'] = f"<p class='green log_entry'>Earned {gold_this_turn} golds from the {request.POST['location']} ({time})\n</p>" + \
            request.session['activity_log']
        request.session['increase'] = False
    else:
        request.session['gold'] -= gold_this_turn
        request.session['activity_log'] = f"<p class='red log_entry'>Entered a {request.POST['location']} and lost {gold_this_turn} golds... Ouch. ({time})\n</p>" + \
            request.session['activity_log']
        request.session['increase'] = False

    return redirect('/')


def reset(request):
    if 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activity_log'] = ""
        return redirect('/')
