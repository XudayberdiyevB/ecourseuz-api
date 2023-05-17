from rest_framework import serializers

from common.models import ApplicationForm
from common.models import Category


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['name', 'email', 'category']


class CategoryListSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Category
        fields = '__all__'
