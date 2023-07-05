import pytest
from django.urls import reverse

from common.models import Blog


@pytest.mark.django_db
class TestApplicationFormView:
    def test_create_application_form1(self, client):
        url = reverse('common:application-form')
        data = {
            'course_id': 1,
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'is_answer': False
        }

        response = client.post(url, data=data)
        assert response.status_code == 201


class TestBlogView:
    @pytest.mark.django_db
    def test_blog_list(self, client, new_blog):
        url = reverse("common:blog-list")

        response = client.get(url)

        assert response.status_code == 200
        assert len(response.data) == Blog.objects.count()
        assert response.data[0]["title"] == new_blog.title
