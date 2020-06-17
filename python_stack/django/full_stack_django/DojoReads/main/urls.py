from django.urls import path
from . import views

urlpatterns = [
    # Main Page
    path('', views.index),

    # New Book (render form)
    path('new', views.new),

    # Create the Book and add to database
    path('create', views.create),

    # Create a review (for existing book - from show book page)
    path('<id>/review/create', views.create_review),

    # Show a book
    path('<id>', views.show),

    # show a user
    path('user/<id>', views.show_user),

    # delete a review
    path('review/<id>/delete', views.delete_review),

]
