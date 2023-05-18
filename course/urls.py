from django.urls import path
from .views import (
    CourseApplyUpdateView,
    CourseApplyDeleteView,
    CourseApplyCreateView,
    CourseApplyRetrieveView
)

urlpatterns = [
    path("", CourseApplyCreateView.as_view(), name="course_apply_create"),
    path("<int:pk>/", CourseApplyRetrieveView.as_view(), name="course_apply_read"),
    path("<int:pk>/edit/", CourseApplyUpdateView.as_view(), name="course_apply_edit"),
    path("<int:pk>/delete/", CourseApplyDeleteView.as_view(), name="course_apply_delete")
]
