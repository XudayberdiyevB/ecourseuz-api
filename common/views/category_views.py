from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from common.models import Category
from common.serializers.category_serializers import CategoryListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


