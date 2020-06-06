from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.add_show),
    path('create', views.create_show),
    path('<id>/edit', views.edit_show),
    path('<id>/update', views.update_show),
    path('<id>', views.display_show),

    # path('shows', views.index),
    # path('shows/new', views.add_show),
    # path('shows/create', views.create_show),
    # path('shows/<id>/edit', views.edit_show),
    # path('shows/<id>/update', views.update_show),
    # path('shows/<id>', views.display_show),

]
