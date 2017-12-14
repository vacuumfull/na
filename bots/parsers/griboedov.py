import json
import time
import datetime
import config
from grab import Grab
from grab.spider import Task, Spider


class GriboedovSpider(Spider):

    base_url = "http://www.griboedovclub.ru/"
    initial_urls = [base_url + "board/?mo=13"]
    upload_dir = "static/images/"
    filters = ['techno']


    def task_initial(self, grab, task):  
        """Initial task."""
        print("Loaded griboedov events page")
        counter = 0
      
        for elem in grab.doc.select(config.Griboedov.main_path):
            text = elem.text()
            text = text.replace('\n\n','\n')
            if not elem.text():
                counter+=1

        print(counter)
    
    def task_load_info(self, grab,          
                       task, **kwargs):    
        print('hi')


if __name__ == "__main__":
    BOT = GriboedovSpider()
    BOT.run()