from django.db import models
from django.utils.text import slugify


class SocialMedia(models.Model):
    class SocialChoices(models.TextChoices):
        FACEBOOK = 'facebook'
        YOUTUBE = 'youtube'
        INSTAGRAM = 'instagram'
        WHATSAPP = 'whatsapp'
        TELEGRAM = 'telegram'

    type = models.CharField(max_length=100, choices=SocialChoices.choices, default='', unique=True)
    name = models.CharField(max_length=100, blank=True, unique=True)
    urls = models.URLField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = slugify(self.type)
        super(SocialMedia, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'SocialMedia'
