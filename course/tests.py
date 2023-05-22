from django.test import TestCase
from django.urls import reverse
from django.test import Client
from course.models import CourseApply, Course
from users.models import User

client = Client()


class TestCourseApply(TestCase):
    def setUp(self) -> None:
        self.course = Course.objects.create(name="Courses")
        self.user = User.objects.create(username="Farruxbek", email="yunusboyevfarruxbek@gmail.com")
        new_course = {
            "status": "new stats",
            "course": self.course.id,
            "users": self.user.id
        }


