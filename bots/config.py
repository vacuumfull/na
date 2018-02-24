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
	fest_path = "//div[@class='view-content']/table/tbody/tr/td"
	header_path = "article/header/h2/a/@href"
	pagers_path = "//ul[@class='pager']//li[@class='pager-item']//a"
	img_path = "//div[@class='field-name-field-image']//div[@class='field-items']//div[@class='field-item']"
	content_path = "//div[@id='content']//article//div[@class='field field-name-body field-type-text-with-summary field-label-above']//div[@class='field-items']"
	date_start = "//div[@class='field field-name-field-date field-type-datetime field-label-inline clearfix']//div[@class='field-items']//div[@class='field-item']//span[@class='date-display-range']//span[@class='date-display-start']/@content"
	date_end = "//div[@class='field field-name-field-date field-type-datetime field-label-inline clearfix']//div[@class='field-items']//div[@class='field-item']//span[@class='date-display-range']//span[@class='date-display-end']/@content"
	address_path = "//div[@class='field-name-field-adress']//div[@class='field-items']//div[@class='field-item']"
	contacts_path = "//div[@class='field-name-field-kontacts']//div[@class='field-items']//div[@class='field-item']"
	site_path = "//div[@class='field-name-field-link']//div[@class='field-items']//div[@class='field-item']"