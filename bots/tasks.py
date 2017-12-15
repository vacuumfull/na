from django.core.cache import cache
from under.celery import app


@app.task(name='bots.tasks.get_parsed_result')
def get_parsed_result(result):
    print(result)
