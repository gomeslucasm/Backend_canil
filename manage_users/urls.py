from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path, include
from .views import *


urlpatterns = [
    ### Token views
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ### Registro de usuários
    path('users/staff/', StaffUserView.as_view({'get':'list','post':'create'}), name = 'register_staff'),
    path('users/', UserView.as_view({'get':'list'}), name = 'register_staff'),
    path('users/volunteer/', VolunteerUserView.as_view({'get':'list','post':'create'}), name = 'register_volunteer'),
    path('users/veterinary/', VeterinaryUserView.as_view({'get':'list','post':'create'}), name = 'register_veterinary'),
    path('users/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
]   