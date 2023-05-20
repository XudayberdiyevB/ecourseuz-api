from django.db import models
from django.utils.text import slugify

from common.models.base import BaseModel
from users.models import User


class Blog(BaseModel):
    title = models.CharField(max_length=255, null=True, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    views_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name_plural = 'Blog'
