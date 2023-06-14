from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response

from common.models import Category
from common.serializers import CategoryListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers

    def list(self, request, *args, **kwargs):
        cached_categories = cache.get("categories")
        if not cached_categories:
            data = self.serializer_class(self.get_queryset(), many=True).data
            cache.set("categories", data, timeout=30)
            cached_categories = cache.get("categories")
        return Response(cached_categories)
