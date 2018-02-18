import json
import time
import datetime
import copy
from event.tasks import check_with_cache
from bots.config import Allfest
from grab import Grab
from bs4 import BeautifulSoup
from grab.spider import Task, Spider

class AllfestSpider(Spider):

	base_url = 'http://all-fest.ru'
	initial_urls = [base_url + "/allfest/"]
    upload_dir = "static/images/"

	def task_initial(self, grab, task):
		pass