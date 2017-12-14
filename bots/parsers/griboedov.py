import json
import time
import datetime
import config
from grab import Grab
from bs4 import BeautifulSoup
from grab.spider import Task, Spider


class GriboedovSpider(Spider):

    base_url = "http://www.griboedovclub.ru/"
    initial_urls = [base_url + "board/"]
    upload_dir = "static/images/"
    filters = ['techno']


    def task_initial(self, grab, task):  
        """Initial task."""
        print("Loaded griboedov events page")
        counter = 0
        for elem in grab.doc.select(config.Griboedov.main_path):
            text = elem.text()
            text = text.replace('\n\n','\n')
            counter+=1
            if len(elem.text()) > 0:
                p_count = 0    
                for p in elem.select("p"):
                    p_count+=1
                    has_title = p.select("a/strong").exists()
                    if has_title:
                        try:
                            print(p.text())
                            html = elem.select("p")[p_count].html()
                            link = self.get_href(html)
                            src = self.get_img_src(html)
                        except IndexError:
                            pass
                        
           
    
    def task_load_info(self, grab,          
                       task, **kwargs):    
        print('hi')


    @staticmethod
    def get_href(html):
        href = ""
        soup = BeautifulSoup(html)
        for a in soup.find_all('a', href=True):
            href = a['href']
        print(href)
        return href

    @staticmethod
    def get_img_src(html):
        src = ""
        soup = BeautifulSoup(html)
        for img in soup.find_all('img', src=True):
            src = img['src']
        print(src)
        return src


if __name__ == "__main__":
    BOT = GriboedovSpider()
    BOT.run()