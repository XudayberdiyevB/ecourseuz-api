from django.urls import path
from course.views import (
    CourseApplyView,
    CourseApplyDetailView
)

urlpatterns = [
    path("course-apply/", CourseApplyView.as_view(), name="course_apply"),
    path("course-apply/<int:pk>/", CourseApplyDetailView.as_view(), name="course_apply_detail"),
]
