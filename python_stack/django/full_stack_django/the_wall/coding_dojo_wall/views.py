from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from coding_dojo_wall.models import *


def index(request):
    # return HttpResponse('Inside the CODING DOJO WALL index method')

    # Get all the posted messages for the currently logged in user (request.session['user_id'])
    all_messages = Message.objects.filter(user=request.session['userid'])

    context = {
        'all_messages': all_messages,
    }

    return render(request, 'index.html', context)


def create_message(request):
    print('Inside new_message view method')
    print('request.POST', request.POST)
    print('request.session[first_name]', request.session['first_name'])
    print('request.session[id]', request.session['userid'])

    # Create a message object...
    this_message = Message(
        user_id=request.session['userid'], message=request.POST['message'])

    # TODO: Remove after testing
    print('this_message.user_id', this_message.user_id)
    print('this_message.message', this_message.message)

    # Save the message object...
    this_message.save()

    return redirect('/wall')
