from django.urls import path
from course.views import CourseApiView

urlpatterns = [
    path("course/", CourseApiView.as_view(), name="course-api")
]
