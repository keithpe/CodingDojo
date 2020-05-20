from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('keith/<str:my_name>', views.yet_another),
]
