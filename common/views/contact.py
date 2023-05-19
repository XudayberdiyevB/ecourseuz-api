from rest_framework import generics

from common.models import ContactUs, ContactForm
from common.serializers import ContactUsListSerializers, ContactFormListSerializers


class ContactUsListApiView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsListSerializers


class ContactFormListApiView(generics.ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormListSerializers
