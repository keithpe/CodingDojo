# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_message', views.create_message),
    path('create_comment', views.create_comment),
]
