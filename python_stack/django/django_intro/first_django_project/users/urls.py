from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('register/', views.register),
    path('login/', views.login),
]
