from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_books),
    path('new', views.create_book),
    path('<id>', views.show_book),
    path('<id>/edit', views.edit_book),
    path('<id>/add_to_favorites', views.add_to_favorites),
]
