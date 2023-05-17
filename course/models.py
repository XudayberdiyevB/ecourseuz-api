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
    is_public = models.BooleanField(choices=CHOICES_PUBLIC)
    time = models.TimeField(auto_now_add=True)
    course_id = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course_content'
    )
    position = models.IntegerField()

    def __str__(self):
        return self.title


class ApplyStatus(models.Choices):
    UNPAID = 'Unpaid', "unpaid"
    PAID = 'Paid', "paid"


class Rate(models.Choices):
    CHOICE_ONE = 1
    CHOICE_TWO = 2
    CHOICE_THREE = 3
    CHOICE_FOUR = 4
    CHOICE_FIVE = 5


class CourseApply(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user"
    )
    status = models.CharField(max_length=20, choices=ApplyStatus.choices)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Review(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course"
    )
    rate = models.PositiveIntegerField(max_length=20, choices=Rate.choices)
    comment = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class CourseTag(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='tag'
    )
