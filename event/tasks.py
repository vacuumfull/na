# event/tasks.py
from event.models import Event
from under.celery import app
from django.core.cache import cache

@app.task(name='event.tasks.events_to_cache')
def events_to_cache():
    events = Event.objects.values('id', 'title', 'date')
    list_result = [i for i in events]
    cache.set('event_titles', list_result, 3600*24)