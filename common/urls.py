from django.urls import path

from .views import AboutUsListApiViews, ContactUsListApiView, ContactFormListApiView, SocialMediaList, \
    CategoryListApiViews, ApplicationFormView, SocialMediaDetail, BlogList, BlogDetail

urlpatterns = [
    path('application-form/', ApplicationFormView.as_view(), name='application-form'),
    path('category/', CategoryListApiViews.as_view(), name='category-list'),
    path('about-us/', AboutUsListApiViews.as_view(), name='about-us'),
    path('contact/', ContactUsListApiView.as_view(), name='contact-us'),
    path('contact-form/', ContactFormListApiView.as_view(), name='contact-form'),
    path('social-media/', SocialMediaList.as_view(), name='social-media-list'),
    path('social-media/<int:pk>/', SocialMediaDetail.as_view(), name='social-media-detail'),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]
