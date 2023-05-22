from django.db import models

from common.models import BaseModel


class Banner(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banner/images')
    position = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Banner'
