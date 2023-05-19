from rest_framework import serializers

from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'desc', 'price', 'discount', 'level', 'author', 'category', 'image', 'video')
