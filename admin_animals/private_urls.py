from django.urls import path, include
from .private_views import *

urlpatterns = [
    ############# Animals view
    path('private/animal/', AnimalViewSet.as_view({'get':'list','post':'create'}), name='animal_list'),
    path('private/animal/<int:pk>/', AnimalViewSet.as_view({'get':'retrieve'}), name='animal_retrieve'),
    ############# Operations view
    path('private/operation/', OperationViewSet.as_view({'get':'list','post':'create'}), name='operation_list'),
    path('private/operation/<int:pk>/', OperationViewSet.as_view({'get':'retrieve'}), name='operation_retrieve'),
    ############# Operations info view
    path('private/operation/info/<int:pk>/', OperationInfoViewSet.as_view({'get':'retrieve'}), name='operation_info_retrieve'),
    path('private/operation/info/', OperationInfoViewSet.as_view({'get':'list','post':'create'}), name='operation_info_list'),
    #############
    path('private/animal/operation/', AnimalWithOperationInfoViewSet.as_view({'get':'list'}), name='animal_w_operation_list'),
    path('private/animal/<int:pk>/operation/', AnimalWithOperationInfoViewSet.as_view({'get':'retrieve'}), name='animal_w_operation_retrieve'),
    
]