from django.shortcuts import render


def index(request):

    # Using gmtime() is the way the assignment suggested we retrieve the date and time
    from time import gmtime, strftime

    context = {
        "time": strftime("%b %m, %Y  %I:%M %p", gmtime())
    }

    # Using datetime.now() is another way to retrieve the date and time
    from datetime import datetime

    context2 = {
        "time": datetime.now().strftime("%b %m, %Y  %I:%M %p")
    }
    return render(request, 'index.html', context2)
