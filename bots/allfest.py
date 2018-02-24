import json
import time
import datetime
import copy
from bots.config import Allfest
from grab import Grab
from bs4 import BeautifulSoup
from grab.spider import Task, Spider


class AllfestSpider(Spider):

	base_url = 'http://all-fest.ru'
	initial_urls = [base_url + "/allfest/"]
	upload_dir = "static/images/"

	def task_initial(self, grab, task):
		print('Loaded main page')
		print(grab.doc.select(Allfest.fest_path).exists())
		for elem in grab.doc.select(Allfest.fest_path):	
			page_uri = elem.select(Allfest.header_path).text()
			yield Task('open_page', url=self.base_url + page_uri)


	def task_open_page(self, grab, task, **kwargs):
		time.sleep(3)
		self.load_content(task.url, Allfest.content_path)


	def task_load_info(self, grab, task, **kwargs):
		print(task.url)



		


	def load_content(self, url, path):
		"""Load content from url"""
		grabber = Grab()
		grabber.go(url)
		print(grabber.doc.select(path).exists())
	#	html = grabber.doc.select(path).html()
	#	print(html)
		#return html

if __name__ == 'main':
	bot = AllfestSpider()
	bot.run()