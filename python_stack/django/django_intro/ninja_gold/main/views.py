from django.shortcuts import render, HttpResponse


def index(request):
    # return HttpResponse("Ninja Gold")
    return render(request, 'index.html')
