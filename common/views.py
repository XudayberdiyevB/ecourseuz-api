from rest_framework import generics

from common.models import Category, ContactUs, ContactForm
from common.models.application_form import ApplicationForm
from .serializers import ApplicationFormSerializer, CategoryListSerializers, ContactUsListSerializers, \
    ContactFormListSerializers


class CategoryListApiViews(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializers


class ApplicationFormView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer


class ContactUsListApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsListSerializers


class ContactFormListApiView(generics.ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormListSerializers
