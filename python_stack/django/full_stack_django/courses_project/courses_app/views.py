from django.shortcuts import render, redirect, HttpResponse
from courses_app.models import *
from django.contrib import messages


def show_courses(request):
    all_courses = Course.objects.all()
    context = {'all_courses': all_courses}
    print('all_courses', all_courses)

    return render(request, "index.html", context)


def add_course(request):
    # Add new course
    if request.POST:
        print("Inside ADD COURSE POST method")
        print('request.POST=', request.POST)
        errors = Course.objects.basic_validator(request.POST)
        if errors:
           # Loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)

            print('errors', errors)

            # Save form info so we can display it back in the form when we get redirected.
            request.session['name'] = request.POST['name']
            request.session['description'] = request.POST['description']

            # redirect the user back to the form to fix the errors
            return redirect('/new')

        # Create new course
        this_desc = Description(text=request.POST['description'])
        this_desc.save()

        this_course = Course(name=request.POST['name'], description=this_desc)
        this_course.save()

        # Blank session values after we successfully add a record.
        request.session['name'] = ''
        request.session['description'] = ''

    else:
        print("Inside ADD COURSE, NOT A POST method")

    return redirect('/show')


def delete_course(request, id):
    print('request.POST', request.POST, id)

    # Get the record we want to delete and pass it to delete.html
    this_course = Course.objects.get(id=id)
    context = {'this_course': this_course}

    return render(request, "delete.html", context)


def destroy_course(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/show')


def show_comments(request, id):
    # Change this filter it needs to filter for course.id = id
    this_course = Course.objects.get(id=id)
    these_comments = Comment.objects.filter(course_id=id)
    context = {'these_comments': these_comments,
               'this_course': this_course}

    return render(request, "comments.html", context)


def add_comment(request, id):
    this_course = Course.objects.get(id=id)
    this_comment = Comment(text=request.POST['comment'])
    this_comment.course_id = id
    this_comment.save()
    this_course.comment = this_comment
    this_course.save()

    print('about to redirect to comments')
    return redirect('/'+str(this_course.id)+'/comments')


def delete_comment(request, id):
    this_comment = Comment.objects.get(id=id)
    course_id = this_comment.course_id
    Comment.objects.filter(id=id).delete()
    return redirect('/'+str(course_id)+'/comments')
