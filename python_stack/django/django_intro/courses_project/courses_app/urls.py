from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_courses),
    path('show', views.show_courses),
    path('new', views.add_course),
    path('<id>/delete', views.delete_course),
    path('<id>/destroy', views.destroy_course),
    path('<id>/comments', views.show_comments),
    path('<id>/new_comment', views.add_comment),
]
