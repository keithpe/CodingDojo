from django.shortcuts import render, redirect, HttpResponse


def show_courses(request):
    return render(request, "index.html")


def add_course(request):
    # Add new course
    if request.POST:
        print("Inside ADD COURSE POST method")
    else:
        print("NOT A POST")

    return redirect('/show_courses')
