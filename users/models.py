from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from .managers import CustomUserManager

AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google', 'email': 'email'}


class User(AbstractUser):
    class UserTypes(models.TextChoices):
        STUDENT = 'student'
        TEACHER = 'teacher'
        SUPERVISOR = 'supervisor'

    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(unique=True, null=True)
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

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }


class SocialAccount(models.Model):
    class ProviderTypes(models.TextChoices):
        GOOGLE = "google"
        FACEBOOK = "facebook"

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="social_account", null=True)
    social_account = models.CharField(max_length=50, choices=ProviderTypes.choices)


class VerificationCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="verification_codes", null=True, blank=True
    )
    email = models.EmailField(unique=True, null=True)
    # verification_type = models.CharField(max_length=50, choices=VerificationTypes.choices)
    last_sent_time = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    expired_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email

    @property
    def is_expire(self):
        return self.expired_at < self.last_sent_time + timedelta(seconds=30)
