from django.urls import path, include
from .public_views import *

# Private urls

urlpatterns = [
    #############
    # Public views
    #############
    path('public/animals/', AnimalViewSet.as_view({'get':'list'}), name='animal_list'),
    path('public/animals/<int:pk>/', AnimalViewSet.as_view({'get':'retrieve'}), name='animal_retrieve'),
]