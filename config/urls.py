from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="e-course.uz API",
        default_version='v1',
        description="API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@p10.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls'), name='common'),
    path('user/', include('users.urls'), name='user'),
    path('course/', include('course.urls'), name='course'),
]

swagger = [
    re_path(r'api(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += swagger
