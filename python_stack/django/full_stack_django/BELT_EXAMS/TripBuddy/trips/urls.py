from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:id>/edit', views.edit),
    path('update', views.update),
]
