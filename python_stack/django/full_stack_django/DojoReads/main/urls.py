from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('create_review/<id>', views.create_review),
    path('<id>', views.show),
    path('user/<id>', views.show_user),

]
