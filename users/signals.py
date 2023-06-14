from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import VerificationCode


@receiver(post_save, sender=VerificationCode)
def update_code_expire_at(sender, instance, **kwargs):  # noqa
    expired_at = instance.last_sent_time + timedelta(seconds=60)
    VerificationCode.objects.filter(id=instance.id).update(expired_at=expired_at)
