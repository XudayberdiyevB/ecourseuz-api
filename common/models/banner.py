from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banner/images')
    position = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=False)
