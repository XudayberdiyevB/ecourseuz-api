from django.urls import path
from .views import (
    CourseApplyView,
    CourseApplyDetailView
)

urlpatterns = [
    path("course-apply/", CourseApplyView.as_view(), name="course_apply"),
    path("course-apply/<int:pk>/", CourseApplyDetailView.as_view(), name="course_apply_detail"),
    # path("<int:pk>/edit/", CourseApplyUpdateView.as_view(), name="course_apply_edit"),
    # path("<int:pk>/delete/", CourseApplyDeleteView.as_view(), name="course_apply_delete")
]
