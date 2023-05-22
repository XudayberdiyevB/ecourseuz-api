from rest_framework import serializers

from common.models import Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', ]


class CategoryListSerializers(serializers.ModelSerializer):
    children = CategorySerializers(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'slug', 'position', 'children']
