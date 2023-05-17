from rest_framework import generics

from common.models.application_form import ApplicationForm
from common.serializers import ApplicationFormSerializer


class ApplicationFormView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
