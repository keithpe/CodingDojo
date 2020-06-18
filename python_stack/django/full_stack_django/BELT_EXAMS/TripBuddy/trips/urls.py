from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:id>/edit', views.edit),
    path('<int:id>/update', views.update),
    path('update', views.update),
    path('<int:id>', views.show),
    path('<int:id>/delete', views.delete),
    path('<int:id>/join', views.join),
    path('<int:id>/cancel', views.cancel),
]
