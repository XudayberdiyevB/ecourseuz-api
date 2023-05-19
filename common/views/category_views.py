from rest_framework import generics

from common.models import Category
from common.serializers import CategoryListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers
