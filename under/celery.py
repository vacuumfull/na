import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'under.settings')
 
app = Celery('under')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'add-daily-at-nine': {
        'task': 'event.tasks.events_to_cache',
        'schedule': crontab(minute=0, hour=9)
    }
}
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()