from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from common.models.category import Category
from common.models import BaseModel


class Course(BaseModel):
    class CourseLevels(models.TextChoices):
        BEGINNER = "beginner", _("Beginner")
        INTERMEDIATE = "intermediate", _("Intermediate")
        ADVANCED = "advanced", _("Advanced")

    name = models.CharField(max_length=250)
    slug = models.SlugField()
    desc = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    level = models.CharField(max_length=32, choices=CourseLevels.choices, default=CourseLevels.BEGINNER)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses_authored'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    image = models.ImageField(upload_to='course_picture/', blank=True, null=True)
    video = models.FileField(upload_to='course_video/', blank=True, null=True)

    def __str__(self):
        return self.name


class CourseContent(BaseModel):
    CHOICES_PUBLIC = [
        (True, 'YES'),
        (False, 'NO')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    is_public = models.BooleanField(choices=CHOICES_PUBLIC)
    time = models.TimeField(auto_now_add=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='contents'
    )
    position = models.IntegerField()

    def __str__(self):
        return self.title


class ApplyStatus(models.Choices):
    UNPAID = _("Unpaid")
    PAID = _("Paid")


class Rate(models.Choices):
    CHOICE_ONE = 1
    CHOICE_TWO = 2
    CHOICE_THREE = 3
    CHOICE_FOUR = 4
    CHOICE_FIVE = 5


class CourseApply(BaseModel):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="applies"
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="course_applies"
    )
    status = models.CharField(max_length=20, choices=ApplyStatus.choices)

    def __str__(self):
        return str(self.user)


class Review(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rate = models.IntegerField(choices=Rate.choices)
    comment = models.CharField(max_length=400)

    def __str__(self):
        return str(self.user)