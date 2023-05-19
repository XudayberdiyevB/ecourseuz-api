from django.urls import path

from course.views import (
    CourseApiView,
    CourseApplyView,
    CourseApplyDetailView,
    CourseContentApiView,
    CourseContentDetilView
)


urlpatterns = [
    path("course/", CourseApiView.as_view(), name="course-api")
    path("course-apply/", CourseApplyView.as_view(), name="course_apply"),
    path("course-apply/<int:pk>/", CourseApplyDetailView.as_view(), name="course_apply_detail"),
    path("course-content/", CourseContentApiView.as_view(), name="course_content"),
    path("course-content/<int:pk>/", CourseContentDetilView.as_view(), name="course_conten-detil"),
]
