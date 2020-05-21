from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('processResults', views.processResults),
    path('showResults', views.showResults),
]
