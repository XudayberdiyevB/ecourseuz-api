from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from common.models import Log
from course.models import Course
from course.serializers import CourseSerializerForLog


@receiver(pre_delete, sender=Course)
def save_course_data_to_log(sender, instance, **kwargs):  # noqa
    content_type = ContentType.objects.get_for_model(Course)
    old_data = CourseSerializerForLog(instance).data
    Log.objects.create(
        content_type=content_type,
        object_id=instance.id,
        action=Log.Actions.DELETE,
        data=old_data
    )
