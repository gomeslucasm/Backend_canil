from django.urls import path
from .views import *

urlpatterns = [
    path('private/adopters/',
         AdopterViewSet.as_view({'get': 'list', 'post': 'create'}), name='animal_list'),
    path('private/adopters/<int:pk>/', AdopterViewSet.as_view(
        {'get': 'retrieve', 'put': 'partial_update'}), name='animal_list'),
    path('private/adoptions/',
         AdoptionViewSet.as_view({'get': 'list', 'post': 'create'}), name='animal_list'),
    path('private/adoptions/<int:pk>/',
         AdoptionViewSet.as_view({'get': 'retrieve'}), name='animal_list'),
    path('private/adopters/animals/', AdopterWithAnimalViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='animal_list'),
    path('private/adopters/animals/<int:pk>/',
         AdopterWithAnimalViewSet.as_view({'get': 'retrieve'}), name='animal_list'),
]
