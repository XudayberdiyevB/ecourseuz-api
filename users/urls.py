from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.social_login.views import GoogleSocialAuthView, FacebookSocialAuthView
from users.views import (
    ProfileView,
    RegisterView,
    SendEmailVerificationCodeView,
    CheckEmailVerificationCodeView,
    CheckEmailVerificationCodeWithParams,
    CustomTokenObtainPairView
)

urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/faceobok/', FacebookSocialAuthView.as_view(), name='facebook_login'),
    path('auth/google/', GoogleSocialAuthView.as_view(), name='google_login'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email/verification/", SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("email/check-verification-code/", CheckEmailVerificationCodeWithParams.as_view(), name="check-email"),
]
