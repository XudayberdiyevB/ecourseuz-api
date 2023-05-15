from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    job = models.CharField(max_length=129)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True,
                                        default='../media/profile_picture/default.png')
    address = models.CharField(max_length=256)
    birth_date = models.DateField(null=False)
    age = models.IntegerField(null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return self.get_full_name()
