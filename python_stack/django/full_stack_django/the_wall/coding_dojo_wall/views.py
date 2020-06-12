from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from coding_dojo_wall.models import *


def index(request):
    # return HttpResponse('Inside the CODING DOJO WALL index method')

    # Get all the posted messages for the currently logged in user (request.session['user_id'])
    all_messages = Message.objects.filter(user=request.session['userid'])
    all_users = User.objects.all()

    context = {
        'all_messages': all_messages,
        'all_users': all_users,
    }

    return render(request, 'index.html', context)


def create_message(request):

    # Create a message object...
    this_message = Message(
        user_id=request.session['userid'], message=request.POST['message'])

    # Save the message object...
    this_message.save()

    return redirect('/wall')


def create_comment(request):
    # Create a comment object
    this_comment = Comment(
        user_id=request.session['userid'], message_id=request.POST['message_id'], comment=request.POST['comment'])

    # Save the message object
    this_comment.save()

    return redirect('/wall')
