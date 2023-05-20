from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about/images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'AboutUs'
