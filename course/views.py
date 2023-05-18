from rest_framework import generics
from .models import CourseApply
from .serializers import CourseApplySerializers


class CourseApplyUpdateView(generics.UpdateAPIView):
    queryset = CourseApply.objects.all()
    serializer_class = CourseApplySerializers


class CourseApplyDeleteView(generics.DestroyAPIView):
    queryset = CourseApply.objects.all()


class CourseApplyCreateView(generics.CreateAPIView):
    queryset = CourseApply.objects.all()
    serializer_class = CourseApplySerializers


class CourseApplyRetrieveView(generics.RetrieveAPIView):
    queryset = CourseApply.objects.all()
    serializer_class = CourseApplySerializers
