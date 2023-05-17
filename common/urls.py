from django.urls import path

from common.views.category_views import CategoryListApiViews

urlpatterns = [
    path('category/', CategoryListApiViews.as_view(), name='category-list'),

]
