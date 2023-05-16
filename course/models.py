from django.db import models

from users.models import User
from common.models.category import Category


class Course(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    desc = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    level = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_course'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_course'
    )
    image = models.ImageField(upload_to='course_picture/', blank=True, null=True)
    video = models.FileField(upload_to='course_video/')
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CourseContent(models.Model):
    CHOICES_PUBLIC = [
        ('0', False),
        ('1', True)
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    is_public = models.CharField(max_length=1, choices=CHOICES_PUBLIC)
    time = models.TimeField(auto_now_add=True)
    course_id = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course_content'
    )
    position = models.CharField()

    def __str__(self):
        return self.title
