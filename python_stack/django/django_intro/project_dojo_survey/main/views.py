from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        # val_from_field_one = request.POST["one"]
        name = request.POST["name"]
        location = request.POST["location"]
        language = request.POST["language"]
        comment = request.POST["comment"]
        print('request.POST[]', request.POST)
        context = {
            'name': name,
            'location': location,
            'language': language,
            'comment': comment
        }
    return render(request, 'result.html', context)
