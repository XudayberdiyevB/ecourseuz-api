from datetime import datetime
from io import BytesIO

import pandas as pd
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import Course, CourseApply, CourseContent, Review
from course.serializers import (
    CourseSerializer,
    CourseApplySerializer,
    CourseContentSerializer,
    CourseReviewSerializer, ImportFileSerializer
)


class CourseApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def get(self, request, *args, **kwargs):
        course_applies = Course.objects.all()
        serializer = CourseSerializer(course_applies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)
    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
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


class CourseExportView(APIView):
    def get(self, request):
        columns = {
            "id": "ID",
            "name": "Nomi",
            "desc": "Batafsil ma'lumot",
            "level": "Daraja",
            "price": "Narxi",
            "author__first_name": "author__first_name",
            "author__last_name": "author__last_name"
        }
        df = pd.DataFrame(
            list(
                Course.objects.values(
                    "id", "name", "desc", "level", "price", "author__first_name", "author__last_name"
                )
            ),
            columns=list(columns.keys())
        )
        df["full_name"] = df["author__first_name"] + " " + df["author__last_name"]
        df.drop(columns=["author__first_name", "author__last_name"], inplace=True)
        columns.update({"full_name": "Muallif"})
        df.rename(columns=columns, inplace=True)

        file_like_object = BytesIO()
        df.to_excel(file_like_object, index=False)
        file_like_object.seek(0)  # move to the beginning of file
        response = FileResponse(file_like_object)
        filename = f"Courses_{datetime.now().strftime('%Y%m%d_%H%M')}"
        response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'

        return response


class CourseImportView(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(request_body=ImportFileSerializer)
    def post(self, request):
        serializer = ImportFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = request.FILES.get("file")
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            Course.objects.update_or_create(id=row["ID"], defaults={
                "name": row["Nomi"],
                "desc": row["Batafsil ma'lumot"],
                "price": row["Narxi"],
                "level": row["Daraja"]
            })
        return Response("Course import started.")
