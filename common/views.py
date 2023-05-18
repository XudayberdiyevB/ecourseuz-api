from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from common.models import Category, ContactUs, ContactForm
from common.models.application_form import ApplicationForm
from config import settings
from course.models import Course
from .serializers import ApplicationFormSerializer, CategoryListSerializers, ContactUsListSerializers, \
    ContactFormListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class ApplicationFormView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer

    @swagger_auto_schema(request_body=ApplicationFormSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ApplicationFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        course_id = serializer.validated_data.get("course").id
        print(course_id)
        course = Course.objects.get(id=course_id)
        message = f"course price: {course.price}\n" \
                  f"Level: {course.level}\n" \
                  f"Description: {course.desc}\n"
        subject = course.name
        send_mail(
            subject, message, from_email=settings.EMAIL_HOST_USER, recipient_list=[email]
        )
        return Response({"detail": "Successfully sent email verification code."})


class ContactUsListApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsListSerializers


class ContactFormListApiView(generics.ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormListSerializers
