from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('author/add_book_to_author', views.add_book_to_author),
    path('author/<id>', views.author_full),
    path('book/add_author_to_book', views.add_author_to_book),
    path('book/<id>', views.book_full),
    path('author/<id>', views.author_full),
]
