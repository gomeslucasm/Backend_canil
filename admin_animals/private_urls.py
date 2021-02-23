from django.urls import path, include
from .private_views import *

urlpatterns = [
    ############# Animals view
    path('private/animals/', AnimalViewSet.as_view({'get':'list','post':'create'}), name='animal_list'),
    path('private/animals/<int:pk>/', AnimalViewSet.as_view({
        'get':'retrieve','delete':'destroy','put':'partial_update',
        }), name='animal_retrieve'),
]