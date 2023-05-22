from django.test import TestCase
from django.urls import reverse
from django.test import Client
from course.models import CourseApply, Course
from users.models import User

client = Client()


class TestCourseApply(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.new_course = None

    def setUp(self) -> None:
        self.course = Course.objects.create()
        self.user = User.objects.create()
        self.course_apply = CourseApply.objects.create(
            status="New status",
            course=self.course,
            user=self.user

        )

    new_course = {
        "status": "new stats",
        "course": "new course",
        "user": "new users"
    }

    def test_course_apply_create(self):
        url = reverse("course_apply")

        response = client.post(url, data=self.new_course)

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.status_code, 400)
        self.assertEqual(response.data["title"], self.new_course["title"])

    def test_course_apply_detail(self):
        url = reverse("course_apply_detail", kwargs={"slug": self.course_apply.slug})

        response = client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.course_apply.title, "New product1")

    def test_product_update(self):
        url = reverse("course_apply_detail", kwargs={"slug": self.course_apply.slug})
        data = {
            "status": "string",
            "course": self.course.id,
            "user": self.user.id
        }
        response = client.put(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], data["title"])

    def test_product_delete(self):
        url = reverse("product_detail", kwargs={"slug": self.course_apply.slug})

        response = client.delete(url)

        self.assertEqual(response.status_code, 204)
