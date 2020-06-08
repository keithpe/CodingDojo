from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_courses),
    path('show_courses', views.show_courses),
    path('add_course', views.add_course),
]
