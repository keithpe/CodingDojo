from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_courses),
    path('show', views.show_courses),
    path('new', views.add_course),
]
