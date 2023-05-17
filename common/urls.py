from django.urls import path

from common.views import ApplicationFormView

urlpatterns = [
    path('application-form/', ApplicationFormView.as_view(), name='application-form'),
]
