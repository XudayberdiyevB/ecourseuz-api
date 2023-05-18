from django.urls import path

from users.views import ProfileView, RegisterView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path("profile/", ProfileView.as_view(), name="profile"),
]
