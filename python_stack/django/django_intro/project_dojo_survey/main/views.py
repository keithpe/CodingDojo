from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'index.html')


def processResults(request):
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

        # Assign session values
        request.session['name'] = name
        request.session['location'] = location
        request.session['language'] = language
        request.session['notifications'] = notifications
        request.session['careful_coding'] = careful_coding
        request.session['daily_blog'] = daily_blog
        request.session['comment'] = comment

    return redirect('/showResults')


def showResults(request):
    print('Inside showResults() via redirect')
    print('requestion.session["name"]', request.session['name'])
    return render(request, 'result.html')
