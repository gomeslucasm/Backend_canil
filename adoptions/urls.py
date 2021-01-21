from django.urls import path
from .views import *

urlpatterns = [
    path('private/adopter/', AdopterViewSet.as_view({'get':'list','post':'create'}), name='animal_list'),
    path('private/adopter/<int:pk>/', AdopterViewSet.as_view({'get':'retrieve'}), name='animal_list'),
    path('private/adoption/', AdoptionViewSet.as_view({'get':'list','post':'create'}), name='animal_list'),
    path('private/adoption/<int:pk>/', AdoptionViewSet.as_view({'get':'retrieve'}), name='animal_list'),
    path('private/adopter/animals/', AdopterWithAnimalViewSet.as_view({'get':'list','post':'create'}), name='animal_list'),
    path('private/adopter/animals/<int:pk>/', AdopterWithAnimalViewSet.as_view({'get':'retrieve'}), name='animal_list'),
]