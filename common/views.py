from rest_framework import generics

from common.models import Category
from common.models.application_form import ApplicationForm
from .serializers import ApplicationFormSerializer, CategoryListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class ApplicationFormView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
