from rest_framework import serializers

from common.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'author', 'views_count']
