from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return render(request, 'index.html')


def processResults(request):
    if request.method == "POST":
        print('request.POST[]', request.POST)

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

        # Assign session values
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['notifications'] = request.POST['notifications']
        request.session['careful_coding'] = careful_coding
        request.session['daily_blog'] = daily_blog
        request.session['comment'] = request.POST['comment']

    return redirect('/showResults')


def showResults(request):
    return render(request, 'result.html')
