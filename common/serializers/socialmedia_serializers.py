from rest_framework import serializers

from common.models import SocialMedia


class SocialMediaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = SocialMedia
        fields = ['id', 'name', 'type', 'urls']
