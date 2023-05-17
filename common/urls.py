from django.urls import path

from common.views import ApplicationFormView
from common.views.category_views import CategoryListApiViews


urlpatterns = [
    path('application-form/', ApplicationFormView.as_view(), name='application-form'),
    path('category/', CategoryListApiViews.as_view(), name='category-list'),
]
