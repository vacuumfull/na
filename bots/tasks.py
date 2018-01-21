# bots/tasks.py
import time
from under.celery import app
from django.core.cache import cache
from bots.ponominaly import PonaminaluSpider
from bots.psytribe import PsyTribeSpider
from bots.griboedov import GriboedovSpider


@app.task(name='bots.tasks.ponominaly_task')
def ponominaly_task():
    BOT = PonaminaluSpider()
    BOT.run()
    time.sleep(10)
    BOT.stop()


@app.task(name='bots.tasks.psytribe_task')
def psytribe_task():
    BOT = PsyTribeSpider()
    BOT.run()
    time.sleep(10)
    BOT.stop()


@app.task(name='bots.tasks.griboedov_task')
def griboedov_task():
    BOT = GriboedovSpider()
    BOT.run()
    time.sleep(20)
    BOT.stop()
