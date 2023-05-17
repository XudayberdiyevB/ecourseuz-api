from django.db import models

from common.models import Category


class ApplicationForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='application')
    created_at = models.DateTimeField(auto_now_add=True)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.name
