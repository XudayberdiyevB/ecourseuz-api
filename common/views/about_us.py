from rest_framework import generics

from common.models import AboutUs
from common.serializers import AboutUsSerializer


class AboutUsListApiViews(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
