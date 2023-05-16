from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (TEACHER, 'teacher'),
        (SUPERVISOR, 'supervisor'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    job = models.CharField(max_length=129)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True)
    address = models.CharField(max_length=256, null=True)
    birth_date = models.DateField(null=True)
    age = models.IntegerField(null=True)
    roles = models.ManyToManyField(Role, related_name='role')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return self.get_full_name()
