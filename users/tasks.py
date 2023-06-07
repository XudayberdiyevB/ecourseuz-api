from celery import shared_task

from users.send_code import send_code_to_phone


@shared_task
def send_verification_code(phone, code):
    send_code_to_phone(phone, code)
