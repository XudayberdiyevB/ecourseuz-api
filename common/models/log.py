from django.contrib.contenttypes.models import ContentType
from django.db import models

from common.models import BaseModel


class Log(BaseModel):
    class Actions(models.TextChoices):
        UPDATE = "update"
        DELETE = "delete"

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    action = models.CharField(max_length=50, choices=Actions.choices)
    data = models.JSONField()
    user = models.ForeignKey("users.User", models.CASCADE, "logs", null=True)
