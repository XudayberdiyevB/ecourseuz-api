from django.urls import path
from .views import SocialMediaList, SocialMediaDetail


urlpatterns = [
    path('', SocialMediaList.as_view(), name='social-media-list'),
    path('social-media/<int:pk>/', SocialMediaDetail.as_view(), name='social-media-detail'),
]