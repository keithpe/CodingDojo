from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.add_show),
    path('create', views.create_show),
    path('<id>/edit', views.edit_show),
    path('<id>/update', views.update_show),
    path('<id>/delete', views.delete_show),
    path('<id>', views.display_show),
]
