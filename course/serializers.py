from rest_framework import serializers
from .models import CourseApply


class CourseApplySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CourseApply
        fields = ('id', 'course', 'user', 'status')
