from rest_framework import serializers

from common.models import ApplicationForm, Category


class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = ['name', 'email', 'category']
