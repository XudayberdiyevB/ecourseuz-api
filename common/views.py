from django.shortcuts import render
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from common.models import Category, ContactUs, ContactForm, ApplicationForm, AboutUs, Blog, Banner, SocialMedia
from config import settings
from course.models import Course
from .serializers import ApplicationFormSerializer, AboutUsSerializer, BlogSerializer, SocialMediaSerializer, CategoryListSerializers, ContactUsListSerializers, ContactFormListSerializers, BannerListSerializers


class SocialMediaList(generics.ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class SocialMediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class BannerListApiView(generics.ListAPIView):
    queryset = Banner.objects.order_by("position")
    serializer_class = BannerListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class AboutUsListApiViews(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer    


class ApplicationFormView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer

    @swagger_auto_schema(request_body=ApplicationFormSerializer)
    def create(self, request, *args, **kwargs):
        serializer = ApplicationFormSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        course_id = serializer.validated_data.get("course").id
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


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
