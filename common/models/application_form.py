from django.db import models

from common.models import Category
from common.models.base import BaseModel
from course.models import Course


class ApplicationForm(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='application')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_answer = models.BooleanField(default=False)

    def str(self):
        return self.email
