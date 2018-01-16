# event/tasks.py
import base64
import time
from urllib.error import HTTPError
from urllib.request import urlretrieve
from event.models import Event
from under.celery import app
from django.core.cache import cache


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
        info['image']= upload_image(info['image'])
        if not info['title']:
            info['title'] = 'какое-то событие' 
        Event.objects.create(title=info['title'], description=info['description'], image=info['image'], date=info['date'], owner_id=1, published=False)
        update_cache(events, info)     


def compare(dict1, dict2):
    diff = set(dict1.items()) & set(dict2.items())
    return len(diff)


def update_cache(events, new_dict):
    events.append(new_dict)
    cache.set('event_titles', events, 3600*24)


def format_img_path(img_path):
    """Format image path."""
    img_info = {}
    splited = img_path.split(".")
    #get extension
    ext = splited[len(splited)-1]
    name = str(base64.b64encode(img_path.encode('utf-8')))
    img_info['ext'] = ext
    # срезаем лишние символы
    img_info['name'] = name[3:3]
    return img_info


def upload_image(img_path):
    """Upload image to dir."""
    upload_dir = "upload/parser_images/"
    img_info = format_img_path(img_path)
    target_path = (upload_dir +
                    "_" +
                    img_info.get('name') +
                    '.' +
                    img_info.get('ext'))
    try:
        urlretrieve(img_path, target_path)
        return target_path
    except FileNotFoundError as err:
        print(err)   # something wrong with local path
    except HTTPError as err:
        print(err)  # something wrong with url

