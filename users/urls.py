from django.urls import path

from users.views import (
    ProfileView,
    RegisterView,
    SendEmailVerificationCodeView,
    CheckEmailVerificationCodeView,
    CheckEmailVerificationCodeWithParams
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email/verification/", SendEmailVerificationCodeView.as_view(), name="send-email-code"),
    path("email/check-verification/", CheckEmailVerificationCodeView.as_view(), name="check-email-code"),
    path("email/check-verification-code/", CheckEmailVerificationCodeWithParams.as_view(), name="check-email"),
]
