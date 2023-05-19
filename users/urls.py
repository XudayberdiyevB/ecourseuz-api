from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenObtainPairView, ProfileView, RegisterView

urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
    path('auth/register/', RegisterView.as_view(), name='register'),
    path("profile/", ProfileView.as_view(), name="profile"),
]
