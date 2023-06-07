import os

from celery import Celery
from celery.schedules import crontab

from users.tasks import send_verification_code

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'send-code-to-user': {
        'task': 'config.celery.test',
        'schedule': crontab(hour=18, minute=26, day_of_week=3)
    },
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task
def test():
    send_verification_code.delay("+998945419679", "123456")
