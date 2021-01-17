from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path, include
from .views import StaffUserCreate, VolunteerUserCreate, VeterinaryUserCreate


urlpatterns = [
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/staff/', StaffUserCreate.as_view(), name = 'register_staff'),
    path('register/volunteer/', VolunteerUserCreate.as_view(), name = 'register_volunteer'),
    path('register/veterinary/', VeterinaryUserCreate.as_view(), name = 'register_veterinary')
]