from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        # val_from_field_one = request.POST["one"]
        print('request.POST[]', request.POST)
    return HttpResponse('FORM SUBMITTED')
