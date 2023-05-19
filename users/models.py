from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        STUDENT = 'student'
        TEACHER = 'teacher'
        SUPERVISOR = 'supervisor'

    username = models.CharField(max_length=32, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True)
    job = models.CharField(max_length=129, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    address = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    age = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=UserTypes.choices, default=UserTypes.STUDENT)

    objects = CustomUserManager()

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.type = 'admin'
        super(User, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return self.get_full_name()


class SocialAccount(models.Model):
    class ProviderTypes(models.TextChoices):
        GOOGLE = "google"
        FACEBOOK = "facebook"

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="social_account", null=True)
    social_account = models.CharField(max_length=50, choices=ProviderTypes.choices)
