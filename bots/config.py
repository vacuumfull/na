class Psytribe:
	"""Конфиг html путей элементов"""
	event_path = "//div[@id='fragment-5']/ul[@class='ultabs']/li"
	article_path = "//div[@id='topic_body']//div[@style='margin:1em 2.5em;']"
	link_path = "div/a/@href"
	date_path = "a/strong"
	title_path = "a/@title"
	img_path = "div/a/img/@src"
	tag = "psytribe"


class Griboedov:
	event_path = "//div[@class='real_content']//table[@class='gbook']//tr//td[@class='tbody']"
	date_path = "//tr"
	tag = "griboedov"

class Allfest:
	event_apth = "//h2[@class='node__title']//a"