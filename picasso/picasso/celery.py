import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "picasso.settings")

app = Celery("picasso")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'process_uploaded_file': {
        'task': 'api.tasks.process_uploaded_file',
        'schedule': crontab(minute='*/1'),
    },
}

app.conf.timezone = 'UTC'
