from django.urls import path

from common.views import ApplicationFormView, CategoryListApiViews

urlpatterns = [
    path('application-form/', ApplicationFormView.as_view(), name='application-form'),
    path('category/', CategoryListApiViews.as_view(), name='category-list'),
]
