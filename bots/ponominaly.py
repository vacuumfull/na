import copy
import time
import datetime
from grab.spider import Task, Spider
from event.tasks import check_with_cache

class PonaminaluSpider(Spider):
    # Обязательный аргумент стартовых URL
    # limit = 1000 - ибо, что нас ограничивает забирать всё? ;)
    base_url = "https://spb.ponominalu.ru"
    initial_urls = [base_url + "/ajax/category/concerts?sort_by=date&sort_direction=desc&limit=1000"]
    locations = ['Гештальт', 'Космонавт', 'Зал ожидания', 'Aurora']
    monthes = [{'Янв': '01'}, {'Фев': '02'}, {'Мар': '03'}, {'Апр': '04'},
            {'Май': '05'}, {'Июн': '06'}, {'Июл': '07'}, {'Авг': '08'},
            {'Сент': '09'}, {'Окт': '10'}, {'Нояб': '11'}, {'Дек': '12'}]

    def task_initial(self, grab, task):
        """
        Обязательная первая задача
        Ищем ссылки на подразделы
        """
        print('Load main page')
        for elem in grab.doc.select('//div[@class="events-list"]/div[@class="events-list__item event"]'):
            info_url = self.base_url + elem.select('a/@href').text()
            info = {}
            info['image'] = 'http://' + elem.select('a/img/@src').text().lstrip('/')
            info['title'] = elem.select(
                'article[@class="event__info bs-bx"]/div[@class="event__title"]/a/span').text()
            info['date'] = elem.select(
                'article[@class="event__info bs-bx"]/time[@class="event__time"]').text()
            info['location'] = elem.select(
                'article[@class="event__info bs-bx"]/div[@class="event__venue"]/a/span').text()
            info['description'] = info_url
            for item in self.locations:
                if info['location'].find(item) > -1:
                    yield Task('load_info', url=info_url, info=copy.deepcopy(info))


    def task_load_info(self, grab, task, **kwargs):
        """ Обработка собственно карточки """
        # Тут большая и жирная логика, чего надо збарть уже со страницы, типа аннотаций и рпочего
        # Так как сайт являеться частичным агрегатором, тот тут надо писать условия разные
        print(task.url, task.info)
        shorted = task.info.get('date')[:-6]
        splited = shorted.split(' ')
        day = str(splited[0]) if int(splited[0]) > 9 else '0' + str(splited[0])
        month = ""
        for mon in self.monthes:
            for item in mon.keys():
                if splited[1].find(item.lower()) > -1:
                    month = mon[item]
        date = str(day) + str(month) + str(splited[2])
        print(date)
        task.info['date'] = datetime.datetime.strptime(date, '%d%m%Y').date()
        check_with_cache.delay(task.info)


if __name__ == "__main__":
    # Создание бота на основе нашего Паука
    BOT = PonaminaluSpider()
    BOT.run()