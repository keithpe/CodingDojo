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
