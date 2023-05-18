from django.db import models

from common.models import Category
from common.models.base import BaseModel


class ApplicationForm(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='application')
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
