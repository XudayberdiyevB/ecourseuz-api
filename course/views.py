from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from course.models import CourseApply
from course.serializers import CourseApplySerializer


class CourseApplyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_applies = CourseApply.objects.all()
        serializer = CourseApplySerializer(course_applies, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseApplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CourseApplyDetailView(CourseApplyView):

    def get(self, request, *args, **kwargs):
        course_apply = get_object_or_404(CourseApply, id=kwargs.get('pk'))
        serializer = CourseApplySerializer(course_apply)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        course_apply = get_object_or_404(CourseApply, id=kwargs.get('pk'))
        serializer = CourseApplySerializer(instance=course_apply, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
