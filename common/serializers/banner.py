from rest_framework import serializers

from common.models import Banner


class BannerListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("title", "description", "image")
