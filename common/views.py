from django.shortcuts import render
from rest_framework import generics

from common.models import Banner
from common.serializers import BannerListSerializers


class BannerListApiView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerListSerializers
