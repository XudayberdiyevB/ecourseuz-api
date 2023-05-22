from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class ApplicationFormViewTest(TestCase):
    def test_create_application_form(self):
        url = reverse('application-form')
        data = {
            'course': 1,
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'is_answer': False
        }

        response = client.post(url, data=data)
        self.assertEqual(response.status_code, 201)
