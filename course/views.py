from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

from course.models import CourseApply, CourseContent
from course.serializers import CourseApplySerializer, CourseContentSerializer


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
    permission_classes = [IsAuthenticated]

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


class CourseContentApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        course_content = CourseContent.objects.all()
        serializer = CourseContentSerializer(course_content, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseContentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class CourseContentDetilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_content = get_object_or_404(CourseContent, id=kwargs.get('pk'))
        serializer = CourseContentSerializer(course_content)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        queryset = get_object_or_404(CourseContent, id=kwargs.get('pk'))
        serializer = CourseContentSerializer(instance=queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
