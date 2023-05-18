from django.urls import path


from common.views import ApplicationFormView, CategoryListApiViews, AboutUsListApiViews

urlpatterns = [
    path('application-form/', ApplicationFormView.as_view(), name='application-form'),
    path('category/', CategoryListApiViews.as_view(), name='category-list'),
    path('about-us/',AboutUsListApiViews.as_view(), name='about-us')
]
