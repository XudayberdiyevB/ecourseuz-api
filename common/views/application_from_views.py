from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template import Template
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models import ApplicationForm
from common.serializers.application_form import ApplicationFormSerializer



class ApplicationFormView(APIView):
    queryset = ApplicationForm.objects.all()
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=ApplicationFormSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ApplicationFormSerializer(data=request.data, )
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        email = serializer.validated_data.get("email")
        course_id = serializer.validated_data.get("course_id")
        course = Course.objects.get(id=course_id, )

        self.queryset.get_or_create(name=name, email=email, course_id=course_id)
        message_html = f"course price: {course.price}\n" \
                       f"Level: {course.level}\n" \
                       f"Description: {course.desc}\n"
        subject = f"Course Information CodeKaplan"
        send_mail(subject, message_html, from_email=settings.EMAIL_HOST_USER, recipient_list=[email],
                  fail_silently=False)
        serializer.save()
        return Response({"detail": "Information about the course has been sent by email "})
