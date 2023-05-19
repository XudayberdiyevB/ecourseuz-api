from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# my imports

from django.contrib import admin
from django.urls import path, include


# my imports

from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="P10 Api",
        default_version='v1',
        description="P10",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@p10.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("common.urls"))


]

swagger_urls = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += swagger_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
