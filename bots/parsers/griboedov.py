import json
import time
import datetime
import config
from grab import Grab
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
                        print(p.text())
                        
           
    
    def task_load_info(self, grab,          
                       task, **kwargs):    
        print('hi')


if __name__ == "__main__":
    BOT = GriboedovSpider()
    BOT.run()