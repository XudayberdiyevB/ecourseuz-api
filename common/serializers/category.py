from rest_framework import serializers

from common.models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'position', 'children']


class CategoryListSerializers(serializers.ModelSerializer):
    children = CategorySerializers(many=True, read_only=True)
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'position', 'children']
