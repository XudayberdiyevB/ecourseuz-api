from django.db import models

from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    desc = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    level = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_course'
    )
    image = models.ImageField(upload_to='course_picture/', blank=True, null=True)
    video = models.FileField(upload_to='course_video/')
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
