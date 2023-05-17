from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from common.models import BaseModel, Category


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
        related_name='user_course'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_course'
    )
    image = models.ImageField(upload_to='course_picture/', blank=True, null=True)
    video = models.FileField(upload_to='course_video/')

    def __str__(self):
        return self.name
