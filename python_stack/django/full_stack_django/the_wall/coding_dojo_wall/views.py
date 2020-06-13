from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from coding_dojo_wall.models import *

# Use pytz with datetime.datetime.now() to get timezone aware (UTC as timezone), so th call to now can be
# compared to the created_at date stored in darabase (which also has UTC time zone value)
# now = 2020-06-12 22:14:13.176717+00:00
# rather than now = 2020-06-12 22:14:13.176717
# So we call the now method with tz=pytz.utc
# now = datetime.datetime.now(tz=pytz.utc)
# Used in delete_message method below
import pytz


def index(request):
    # return HttpResponse('Inside the CODING DOJO WALL index method')

    # TODO Should we change this to ONLY retrieve messages going back a month (how big is too big?)
    all_messages = Message.objects.all().order_by('-created_at')
    all_users = User.objects.all()

    context = {
        'all_users': all_users,
        'all_messages': all_messages,
    }

    return render(request, 'index.html', context)


def create_message(request):

    # Create a message object...
    this_message = Message(
        user_id=request.session['userid'], message=request.POST['message'])

    # Save the message object...
    this_message.save()

    return redirect('/wall')


def delete_message(request):

    # Get the message
    this_message = Message.objects.get(id=request.POST['message_id'])

    # Calculate time between now and created_at filed of message record.
    now = datetime.datetime.now(tz=pytz.utc)
    difference = now - this_message.created_at

    # Only delete the message if the difference in seconds (between now and created_at) is less than 1800
    # (30 minutes * 60 (seconds/minute) = 1800)

    # Only allow the user who created this message to delete it AND only if it was created within 30 minutes of now
    if this_message.user_id == request.session['userid'] and (difference.seconds <= 1800):

        # Delete the message
        this_message.delete()

    return redirect('/wall')


def create_comment(request):
    # Create a comment object
    this_comment = Comment(
        user_id=request.session['userid'], message_id=request.POST['message_id'], comment=request.POST['comment'])

    # Save the message object
    this_comment.save()

    return redirect('/wall')


def delete_comment(request):

    # Get the comment
    this_comment = Comment.objects.get(id=request.POST['comment_id'])

    # Only allow the user who created this comment to delete it
    if this_comment.user_id == request.session['userid']:
        # Delete the comment
        this_comment.delete()

    return redirect('/wall')
