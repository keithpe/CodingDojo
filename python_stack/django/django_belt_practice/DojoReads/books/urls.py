from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('create_book', views.create_book),
    path('show_book/<id>', views.show_book),
    path('<id>/add_review', views.add_review),
    path('show_user/<id>', views.show_user),
    path('delete_review/<id>', views.delete_review),
]
