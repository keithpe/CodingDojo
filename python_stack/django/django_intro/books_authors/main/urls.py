from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
]
