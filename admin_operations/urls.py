from django.urls import path
from .views import *

urlpatterns = [
    path('private/operations/', OperationViewSet.as_view({'get':'list'}), name='animal_list'),
    path('private/operations/<int:pk>/', OperationViewSet.as_view({'get':'retrieve'}), name='animal_retrieve'),
    path('private/operations/type/', OperationSeparatedByTypeViewSet.as_view({'get':'list'}), name='animal_list'),
    path('private/operations/type/<int:pk>/', OperationSeparatedByTypeViewSet.as_view({'get':'retrieve'}), name='animal_retrieve'),
    path('private/operations/animal/', OperationSeparatedByAnimalViewSet.as_view({'get':'list'}), name='animal_list'),
    path('private/operations/animal/<int:pk>/', OperationSeparatedByAnimalViewSet.as_view({'get':'retrieve'}), name='animal_retrieve'),
]