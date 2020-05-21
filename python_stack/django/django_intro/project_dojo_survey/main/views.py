from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def result(request):
    if request.method == "POST":
        print('request.POST[]', request.POST)
        name = request.POST["name"]
        location = request.POST["location"]
        language = request.POST["language"]
        notifications = request.POST['notifications']

        # checkbox has no value if not checked. Check for the existance
        # of the dictionary key in the POST[] dictionary.
        if 'careful_coding' in request.POST.keys():
            careful_coding = 'yes'
        else:
            careful_coding = 'no'

        # Checkbox issue, same as above.
        if 'daily_blog' in request.POST.keys():
            daily_blog = 'yes'
        else:
            daily_blog = 'no'

        comment = request.POST["comment"]
        context = {
            'name': name,
            'location': location,
            'language': language,
            'notifications': notifications,
            'careful_coding': careful_coding,
            'daily_blog': daily_blog,
            'comment': comment
        }
    return render(request, 'result.html', context)
