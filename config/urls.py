from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ecourse api",
        default_version='v1',
        description="P10 ecourse API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@p10.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

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

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('common.urls'), name='common'),
    path('course/', include('course.urls'), name='course'),
    path('bot/', include('bot.urls'), name='bot'),
)

swagger_urls = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += swagger_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
