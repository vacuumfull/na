# event/tasks.py
from under.celery import app
from django.core.cache import cache

@app.task(name='bots.tasks.bots_task')
def bots_task():
    cache.set('test', 'list_result', 3600*24)