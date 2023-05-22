from django.urls import path

from course.views import (
    CourseApiView,
    CourseDetailView,
    CourseApplyView,
    CourseApplyDetailView,
    CourseContentApiView,
    CourseContentDetailView,
    CourseReviewApiView,
    CourseReviewDetailView
)


urlpatterns = [
    path("course/", CourseApiView.as_view(), name="course-api"),
    path("course/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("course-apply/", CourseApplyView.as_view(), name="course-apply"),
    path("course-apply/<int:pk>/", CourseApplyDetailView.as_view(), name="course-apply-detail"),
    path("course-content/", CourseContentApiView.as_view(), name="course-content"),
    path("course-content/<int:pk>/", CourseContentDetailView.as_view(), name="course-content-detail"),
    path("course-review/", CourseReviewApiView.as_view(), name="course-review"),
    path("course-review/<int:pk>/", CourseReviewDetailView.as_view(), name="course-review-detail"),
]
