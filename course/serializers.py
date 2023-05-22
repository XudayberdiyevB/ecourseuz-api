from rest_framework import serializers

from course.models import Course, CourseApply, CourseContent, Review


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'desc', 'price', 'discount', 'level', 'author', 'category', 'image', 'video')


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


class CourseReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'user', 'course', 'rate', 'comment')
        