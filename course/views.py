from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from drf_yasg.utils import swagger_auto_schema

from course.models import Course, CourseApply, CourseContent, Review
from course.serializers import (
    CourseSerializer,
    CourseApplySerializer,
    CourseContentSerializer,
    CourseReviewSerializer
)


class CourseApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_applies = Course.objects.all()
        serializer = CourseSerializer(course_applies, many=True)

    @swagger_auto_schema(request_body=CourseSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer( data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CourseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_applies = get_object_or_404(Course, id=kwargs.get('pk'))
        serializer = CourseSerializer(course_applies)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)
    def put(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=kwargs.get('pk'))
        serializer = CourseSerializer(instance=course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CourseApplyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_applies = CourseApply.objects.all()
        serializer = CourseApplySerializer(course_applies, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseApplySerializer)
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

    @swagger_auto_schema(request_body=CourseApplySerializer)
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

    @swagger_auto_schema(request_body=CourseContentSerializer)
    def post(self, request):
        serializer = CourseContentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class CourseContentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_content = get_object_or_404(CourseContent, id=kwargs.get('pk'))
        serializer = CourseContentSerializer(course_content)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseContentSerializer)
    def put(self, request, *args, **kwargs):
        queryset = get_object_or_404(CourseContent, id=kwargs.get('pk'))
        serializer = CourseContentSerializer(instance=queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class CourseReviewApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = CourseReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseReviewSerializer)
    def post(self, request):
        serializer = CourseReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class CourseReviewDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_content = get_object_or_404(Review, id=kwargs.get('pk'))
        serializer = CourseReviewSerializer(course_content)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseReviewSerializer)
    def put(self, request, *args, **kwargs):
        queryset = get_object_or_404(Review, id=kwargs.get('pk'))
        serializer = CourseReviewSerializer(instance=queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
