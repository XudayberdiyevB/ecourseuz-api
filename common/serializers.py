from rest_framework import serializers

from common.models import Banner


class BannerListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Banner
        fields = '__all__'
