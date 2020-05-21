from django.shortcuts import render


def index(request):

    # This is another way to retrieve the date and time
    # print("Inside the index() method")
    # current_time = datetime.datetime.now()
    # print("current_time", current_time)
    # d1 = current_time.strftime("%b %m, %Y")
    # print("d1", d1)

    # This is the way the assignment originally retrieve the date and time
    from time import gmtime, strftime

    context = {
        "time": strftime("%b %m, %Y  %I:%M %p", gmtime())
    }

    # This is another way to retrieve the date and time
    from datetime import datetime

    context2 = {
        "time": datetime.now().strftime("%b %m, %Y  %I:%M %p")
    }
    return render(request, 'index.html', context2)
