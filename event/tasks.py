# event/tasks.py
from event.models import Event
from under.celery import app
from django.core.cache import cache
import time


@app.task(name='event.tasks.events_to_cache')
def events_to_cache():
    events = Event.objects.values('id', 'title', 'date')
    list_result = [i for i in events]
    cache.set('event_titles', list_result, 3600*24)


@app.task(name='event.tasks.check_with_cache')
def check_with_cache(info):
    events = cache.get('event_titles')
    # На проде этот блок надо выпилить, events_to_cache 
    # должен раз в день утром обновлять кэш
    if isinstance(events, type(None)):
        events_to_cache()
        time.sleep(2)
        events = cache.get('event_titles')
        check_or_update(events, info)
    else:
       check_or_update(events, info)


def check_or_update(events, info):
    count = 0
    for item in events:
        if compare(item, info) == 0:
            count += 1
    if count > 0:
        update_cache(events, info)


def compare(dict1, dict2):
    diff = set(dict1.items()) & set(dict2.items())
    return len(diff)


def update_cache(events, new_dict):
    events.append(new_dict)
    cache.set('event_titles', events, 3600*24)
