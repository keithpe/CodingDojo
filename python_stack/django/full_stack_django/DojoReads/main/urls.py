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
    path('<int:id>/review/create', views.create_review),

    # Show a book
    path('<int:id>', views.show),

    # Delete a book
    path('<int:id>/delete', views.delete_book),

    # show a user
    path('user/<int:id>', views.show_user),

    # delete a review
    path('review/<int:id>/delete', views.delete_review),

]
