# bots/tasks.py
import time
from under.celery import app
from django.core.cache import cache
from bots.ponominaly import PonaminaluSpider


@app.task(name='bots.tasks.bots_task')
def ponominaly_task():
    print('hello')
    BOT = PonaminaluSpider()
    BOT.run()
    time.sleep(5)
    BOT.stop()