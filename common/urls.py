from django.urls import path

from common.views import BannerListApiView

urlpatterns = [
    path('banner/', BannerListApiView.as_view(), name='banner')
]