from rest_framework import serializers

from course.models import CourseApply, CourseContent


class CourseApplySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CourseApply
        fields = ('id', 'course', 'user', 'status')


class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = ('title', 'description', 'video', 'is_public', 'time', 'course', 'position')

    read_only_fields = ('id',)
