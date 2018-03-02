import json
import time
import datetime
import copy
from bots.config import Allfest
from grab import Grab
from grab.error import GrabTooManyRedirectsError


class AllfestSpider():

	grabber = Grab()
	base_url = 'http://all-fest.ru/allfest'
	upload_dir = "static/images/"


	monthes = [	{'Янв': '01'}, {'Фев': '02'}, {'Мар': '03'}, {'Апр': '04'},{'Мая': '05'},
				{'Май': '05'}, {'Июн': '06'}, {'Июл': '07'}, {'Авг': '08'},
				{'Сент': '09'}, {'Окт': '10'}, {'Нояб': '11'}, {'Дек': '12'}]


	def load_page(self, uri, def_limit=0):
		try:
			self.grabber.go(self.base_url + uri)
			grdoc = self.grabber.doc
			current = int(grdoc.select(HH.current_page).text())
			if grdoc.select(HH.last_page).exists():
				limit = int(grdoc.select(HH.last_page).text()) - 1
			else:
				limit = def_limit

			for elem in grdoc.select(Allfest.header_path):	
				info = {}
				info['title'] = self.get_path_info(elem, HH.title_path)
				info['date'] = self.get_path_info(elem, HH.date_path)
				info['link'] = self.get_path_info(elem, HH.link_path)
				result['preview_cards'].append(info)
			return result
		except GrabTooManyRedirectsError as e:
			print(e)

	
	
	def load_full_card(self, info):
		"""Load content from url"""
		try:
			self.grabber.go(info.get('link'))
			grdoc = self.grabber.doc
			info['date'] = self.format_date(info.get('date'))
			info['content'] = self.get_path_info(grdoc, HH.content_path, isHtml=True)
			info['employer'] = self.get_path_info(grdoc, HH.employer_name)
			info['salary'] = self.get_path_info(grdoc, HH.vacancy_salary)
			info['address'] = self.get_path_info(grdoc, HH.address_path)
			info['experience'] = self.get_path_info(grdoc, HH.experience_path)
			return info
		except GrabTooManyRedirectsError as e:
			print(e)


	def get_path_info(self, grab, path, isHtml=False):
		isExists = grab.select(path).exists()
		if isExists and isHtml is True:
			return grab.select(path).html()
		elif isExists and isHtml is False:
			return grab.select(path).text()
		else:
			return ""

	def format_date(self, datestring):
		year = '2018'
		splited = datestring.split(' ')
		day = str(splited[0]) if int(splited[0]) > 9 else '0' + str(splited[0])
		month = ""
		for mon in self.monthes:
			for item in mon.keys():
				if splited[1].find(item.lower()) > -1:
					month = mon[item]
		date = str(day) + str(month) + str(year)
		return datetime.datetime.strptime(date, '%d%m%Y').date().isoformat()


if __name__ == 'main':
	bot = AllfestSpider()
	bot.run()