from django.shortcuts import render
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%b %m, %Y  %I:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
