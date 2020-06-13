from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_books),
    path('<id>', views.show_book),
    path('<id>/edit', views.edit_book),
]
