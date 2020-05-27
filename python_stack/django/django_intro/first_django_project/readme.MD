## First Django Project

### Objectives:

- Practice setting up a new Django project
- Practice setting up a new Django app
- Practice routing in Django
- Familiarity with views and how to render a simple HttpResponse

It's time to practice routing! Use the checklist below to add routes to your project. We haven't learned about templates yet, so just return strings via HttpResponse

Even though we don't include the first / in our project urls.py file, when redirecting, you should provide the whole path, starting with the first /.

- [x] Create a new project with a single app / - display the string "placeholder to later display a list of all blogs" with a method named "index"

- [x] /new - display the string "placeholder to display a new form to create a new blog" with a method named "new"

- [x] /create - redirect to the "/" route with a method called "create"

- [x] /int:number - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/15 should display the message: 'placeholder to display blog number 15')

- [x] /int:number/edit - display the string "placeholder to edit blog {number}" with a method named "edit"

- [x] /int:number/delete - redirect to the "/" route with a method called "destroy"

## Multiple Apps

### NOTE:

**This is an update to the original First Django Project. We were tasked with adding other apps.**
**I Chose to remove the original app (app_one), which delt with blogs. And make the root route non functioning (no localhost:8000/)**
**This assignment was to demonstrate the creation of common apps that could be ported to other projects.**

### Objectives:

- Practice creating Django apps
- Get familiar with a Django project with multiple apps

With Django, it's easy to create multiple apps that can be used across multiple projects. Let's say that you're a freelancer and have worked with many clients in the past. Say that almost every single project you've worked on, the client/project wants their own blogs, surveys, and user management system. Instead of having to re-create these modules each time from scratch, you decide to create three independent apps that you can utilize across all of these projects.

Add 2 additional apps, **surveys** and **users** to your project from the First Django Project assignment. (If you've forgotten how to create just an app, refer to all of step 5 (a-e) in the Creating a Django Project module.)

- blogs - update the routes as follows (content is the same):

  - /blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
  - /blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
  - /blogs/create - redirect to the "/blogs" route with a method called "create"
  - /blogs/<number> - display the string "placeholder to display blog number: {{number}}" with a method named "show"
  - /blogs/<number>/edit - display the string "placeholder to edit blog {{number}}" with a method named "edit"
  - /blogs/<number>/delete - redirect to the "/blogs" route with a method called "destroy"

- surveys

  - /surveys - display the string "placeholder to display all the surveys created"
  - /surveys/new - display "placeholder for users to add a new survey"

- users

  - /register - display the string "placeholder for users to create a new user record"
  - /login - display the string "placeholder for users to log in"
  - /users/new - have the same method that handles /register also handle the url request of /users/new
  - /users - display the string "placeholder to later display all the list of users"

**Hint**:

Notice how the blogs and surveys routes all begin with the same pattern, but the users app routes do not. This means our project urls.py file should look something like this:

**project_name/project_name/urls.py**

```python
urlpatterns = [
    path('blogs/', include('apps.blog_app.urls')),
    path('surveys/', include('apps.survey_app.urls')),
    path('users/', include('apps.users_app.urls')),
]
```

**NOTE: The above path values were incorrect in the original assignment instructions on the CodingDojo site. They are correct here.**

Then, in the respective blogs and surveys app urls.py files, we only need to include the remainder of the route to match!

**A reminder about redirecting: you should always provide the whole path, starting with the first /.**

- [x] Add a surveys app and a users app to your first Django project
- [ ] Complete the /blogs route
- [ ] Complete the /blogs/new route
- [ ] Complete the /blogs/create route
- [ ] Complete the /blogs/<number> route
- [ ] Complete the /blogs/<number>/edit route
- [ ] Complete the /blogs/<number>/delete route
- [ ] Complete the /surveys route
- [ ] Complete the /surveys/new route
- [ ] Complete the /register route
- [ ] Complete the /login route
- [ ] Complete the /users/new route
- [ ] Complete the /users route
- [ ] NINJA BONUS: Have the root route utilize the same method as the /blogs route
