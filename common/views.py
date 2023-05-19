from rest_framework import generics
from .models import SocialMedia
from .serializers import SocialMediaSerializer


class SocialMediaList(generics.ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class SocialMediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


