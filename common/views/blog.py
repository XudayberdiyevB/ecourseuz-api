from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated

from common.models import Blog
from common.serializers.blog_serializers import BlogSerializer


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = (AllowAny,)
        return [permission() for permission in self.permission_classes]


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
