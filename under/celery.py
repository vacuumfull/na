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
    },
    'add-daily-at-ten': {
        'task': 'bots.tasks.griboedov_task',
        'schedule': crontab(minute=0, hour=10)
    },
    'twice-a-week-at-ten': {
        'task': 'bots.tasks.psytribe_task',
        'schedule': crontab(hour=10, minute=0, day_of_week=3,5)
    },
    'twice-a-week-at-eleven': {
        'task': 'bots.tasks.ponominaly_task',
        'schedule': crontab(hour=11, minute=0, day_of_week=1,4)
    },
}

app.conf.timezone = 'Europe\Moscow'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()