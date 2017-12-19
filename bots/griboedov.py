import json
import time
import datetime
import copy
from event.tasks import check_with_cache
from bots.config import Griboedov
from grab import Grab
from bs4 import BeautifulSoup
from grab.spider import Task, Spider


class GriboedovSpider(Spider):

    base_url = "http://www.griboedovclub.ru"
    initial_urls = [base_url + "/board/"]
    upload_dir = "static/images/"
    filters = ['techno']


    def task_initial(self, grab, task):  
        """Initial task."""
        print("Loaded griboedov events page")
        now = datetime.datetime.now()
        counter = 0
        for elem in grab.doc.select(Griboedov.event_path):
            text = elem.text()
            text = text.replace('\n\n','\n')
            counter+=1
            if counter > now.day:
                if len(elem.text()) > 0:
                    p_count = 0    
                    for p in elem.select("p"):
                        p_count+=1
                        has_title = p.select("a/strong").exists()
                        if has_title:
                            try:
                                info = {}
                                html = elem.select("p")[p_count].html()
                                day = counter if counter > 9 else '0' + counter
                                date = str(day) + str(now.month) + str(now.year)
                                date = datetime.datetime.strptime(date, '%d%m%Y').date()
                                info['title'] = p.select("a").text()
                                info['link'] = self.get_href(html)
                                info['image'] = self.base_url + self.get_img_src(html)
                                info['date'] = date
                                info['description'] = info['link']
                                yield Task('load_info', url=info['link'], info=copy.deepcopy(info))
                            except IndexError:
                                pass
                        
           
    
    def task_load_info(self, grab,          
                       task, **kwargs):    
        print(task.url, task.info)
        check_with_cache.delay(task.info)


    @staticmethod
    def get_href(html):
        href = ""
        soup = BeautifulSoup(html)
        for a in soup.find_all('a', href=True):
            href = a['href']
        return href

    @staticmethod
    def get_img_src(html):
        src = ""
        soup = BeautifulSoup(html)
        for img in soup.find_all('img', src=True):
            src = img['src']
        return src


if __name__ == "__main__":
    BOT = GriboedovSpider()
    BOT.run()