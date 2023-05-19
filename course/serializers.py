from rest_framework import serializers
from course.models import CourseApply


class CourseApplySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CourseApply
        fields = ('id', 'course', 'user', 'status')
