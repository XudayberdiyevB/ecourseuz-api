from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Course
from .serializers import CourseSerializer


class CourseApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        course_applies = Course.objects.all()
        serializer = CourseSerializer(course_applies, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
