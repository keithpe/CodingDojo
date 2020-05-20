from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is the same as @app.route('/') ")


def yet_another(request, my_name):
    return HttpResponse("my name is: {}".format(my_name))
